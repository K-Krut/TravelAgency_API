import random

from django.db.models import Count
from django.template.loader import render_to_string
from rest_framework.views import exception_handler
from TravelAgency_API import settings
from TravelAgency_API.settings import EMAIL_ADMIN_RECIPIENT, BASE_URL
from liqpayapi.liqpay3 import LiqPay
from .models import *
from django.core.mail import send_mail
from .serializers import TourSerializer


def get_n_most_popular_tours(limit):
    return Tour.objects.all().annotate(order_count=Count('order')).order_by('-order_count')[:limit]


def get_n_most_popular_non_featured_tours(limit):
    return Tour.objects.all().filter(is_featured=False).annotate(order_count=Count('order')).order_by(
        '-order_count')[:limit]


def get_featured_tours(query_size=4):
    queryset_featured = Tour.objects.filter(is_featured=True).annotate(order_count=Count('order')).order_by(
        '-order_count')[:query_size]
    if not queryset_featured:
        return get_n_most_popular_tours(query_size)
    if len(queryset_featured) < query_size:
        return queryset_featured.union(get_n_most_popular_non_featured_tours(4 - len(queryset_featured)))
    return queryset_featured


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['detail'] = 'Incorrect filtering parameter'

    return response


def update_order(response):
    order = Order.objects.get(code=response.get('order_id'))
    order.status = OrderStatus.objects.get(id=4)  # correct id 4
    order.sum_paid = int(response.get('amount')) if response.get('amount') else 0
    order.paytype = response.get('paytype')
    order.sender_card_mask_2 = response.get('sender_card_mask2')
    order.receiver_commission = response.get('receiver_commission')
    order.save()
    return order


def get_liqpay_decoded_response(request):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    data = request.GET.get('data')
    signature = request.GET.get('signature')
    sign = liqpay.str_to_sign(f"{settings.LIQPAY_PRIVATE_KEY} + {data} + {settings.LIQPAY_PRIVATE_KEY}")
    if sign == signature:
        print('callback is valid')
    return liqpay.decode_data_from_str(data)


def get_liqpay_payment_status(response):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    return liqpay.api("request", {
        "action": "status",
        "version": "3",
        "order_id": response.get('order_id')
    })


def get_liqpay_pay_data(request, order, tour):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    params = {
        'action': 'pay',
        'amount': request.data['cost'],
        'currency': 'UAH',
        'description': f'Тур {tour.name} для {len(request.data["passengers"])} пасажирів',
        'order_id': order.code,
        'version': '3',
        'sandbox': 1,
        'server_url': f'{BASE_URL}/pay-callback/',
    }
    signature = liqpay.cnb_signature(params)
    data = liqpay.cnb_data(params)
    return signature, data


def generate_unique_code():
    while True:
        code = random.randint(100000, 999999)
        if not Order.objects.filter(code=code).exists():
            return code


def create_new_order(tour, request):
    code = generate_unique_code()
    return Order.objects.create(
        tour=tour,
        sum=request.data['cost'],
        sum_paid=0,
        code=code,
        status=OrderStatus.objects.get(id=10),  # 10 correct id
    )


def create_order_items(request, order, tour):
    current_free_places = tour.free_places
    for num, passenger in enumerate(request.data['passengers']):
        place_number = current_free_places - num - 1
        OrderItem.objects.create(
            order=order,
            place_number=place_number,
            name=passenger['name'],
            surname=passenger['surname'],
            phone=passenger.get("phone", ""),
            sum=tour.price,
            is_primary_contact=passenger.get('is_primary_contact', False),
            verification_code=random.randint(100000, 999999)
        )


def check_order_cost(tour, request):
    final_cost = tour.price * len(request.data['passengers'])
    return final_cost == request.data['cost']


def check_tour_has_available_places(tour, request):
    return tour.free_places >= len(request.data['passengers'])


def send_mail_(subject, text, recipient=EMAIL_ADMIN_RECIPIENT):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, text, email_from, [recipient])


def send_mail_with_html(subject, context, template_name='email/order_success.html', recipient=EMAIL_ADMIN_RECIPIENT):
    email_from = settings.EMAIL_HOST_USER
    html_content = render_to_string(template_name, context)
    send_mail(subject, '', email_from, [recipient], html_message=html_content)


def send_payment_error_email(response, payment_status):
    send_mail_(
        subject=f"Помилка оплати - {response.get('order_id')}",
        text=f"Помилка оплати замовлення №{response.get('order_id')}\n\nПомилка: {payment_status}"
    )


def get_phone_info(passenger):
    return f"Номер: {passenger.get('phone')}'\n" if passenger.get('phone') else ''


def generate_order_successful_email(data, passengers):
    passengers_info = "-"
    if passengers:
        passengers_info = "\n\n".join([f"Клієнт №{ind + 1}\n"
                                       f"Імʼя: {passenger.get('name')} {passenger.get('surname')}\n"
                                       f"{get_phone_info(passenger)}"
                                       f"Місце: {passenger.get('place')}" for ind, passenger in
                                       enumerate(passengers)])
    return f"Admin, було сформовано нове замовлення\nДеталі замовлення:\n\n" \
           f"Номер замовлення: {data.get('order_code')}\n" \
           f"Сплачена сума: {data.get('sumpaid')} грн\n" \
           f"Назва туру: {data.get('tour').get('name')}\n" \
           f"Дати: {data.get('tour').get('date_start')} - {data.get('tour').get('date_end')}\n\n" \
           f"Пасажири:\n{passengers_info}"


def generate_order_bad_request_email(response, payment_status):
    return f"Хтось намагався зробити запит до API на перевірку статусу оплати " \
           f"та оновлення даних про замовлення в Базі Даних.\n" \
           f"Замовлення №{response.get('order_id')}\n\n" \
           f"Відповідь Liqpay:\n" \
           f"Статус платежу: {payment_status}"


def process_liqpay_payment_info(payment_status):
    return f"ID платежу: {payment_status.get('payment_id')}\n" \
           f"Статус платежу: {payment_status.get('status')}\n" \
           f"Метод оплати: {payment_status.get('paytype')}\n" \
           f"Номер карти: {payment_status.get('sender_card_mask2')}\n" \
           f"Сума платежу: {payment_status.get('amount')}\n" \
           f"Liqpay комісія: {payment_status.get('receiver_commission')}"


def generate_order_server_error_email(response, payment_status):
    return f"Помилка при оновленні інформації про замовлення в Базі Даних\n" \
           f"Замовлення №{response.get('order_id')}\n\n" \
           f"Відповідь Liqpay:\n" \
           f"{process_liqpay_payment_info(payment_status)}"


def update_tour_free_places(tour, places):
    tour.free_places = tour.free_places - places
    tour.save()


def get_passengers_info(order):
    passengers = OrderItem.objects.filter(order=order)
    return [
        {
            'name': passenger.name,
            'surname': passenger.surname,
            'phone': passenger.phone,
            'place': passenger.place_number
        }
        for passenger in passengers
    ]




def get_order_response(order, response):
    tour = Tour.objects.get(pk=order.tour.pk)
    tour_serializer = TourSerializer(tour)

    # обновление количества свободных мест после заказа
    passengers = OrderItem.objects.filter(order=order)
    update_tour_free_places(tour, len(passengers))

    tour_data = tour_serializer.data

    return {
        'tour': tour_data,
        'sumpaid': response.get('amount'),
        'order_code': response.get('order_id')
    }


def get_order_successful_response(order):
    tour = Tour.objects.get(pk=order.tour.pk)
    tour_serializer = TourSerializer(tour)

    return {
        'tour': tour_serializer.data,
        'sumpaid': order.sum_paid,
        'order_code': order.code
    }


def get_client_order_response(order):
    tour = Tour.objects.get(pk=order.tour.pk)
    tour_serializer = TourSerializer(tour)

    return {
        'tour': tour_serializer.data,
        'sumpaid': order.sum_paid,
        'order_code': order.code,
        'passengers': get_passengers_info(order)
    }


def get_user_code(order):
    contact_point = OrderItem.objects.get(order=order, is_primary_contact=True)
    return contact_point.verification_code

