import random
import ssl

from django.shortcuts import redirect
from django.template.loader import render_to_string
from rest_framework.views import exception_handler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from TravelAgency_API import settings
from liqpayapi.liqpay3 import LiqPay
from .models import *
from django.core.mail import send_mail
import smtplib

from .serializers import TourSerializer


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['detail'] = 'Incorrect filtering parameter'

    return response


def create_liqpay_object(final_cost, queryset_name, passengers):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    params = {
        'action': 'pay',
        'amount': final_cost,
        'currency': 'UAH',
        'description': f'{queryset_name} - {passengers} passengers',
        'order_id': random.randint(100000, 999999),
        'version': '3',
        'sandbox': 0,  # sandbox mode, set to 1 to enable it
        'server_url': 'http://127.0.0.1:8000/pay-callback/',  # url to callback view
    }


def update_order(response):
    order = Order.objects.get(code=response.get('order_id'))
    order.status = OrderStatus.objects.get(id=4)
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
            verification_code=order.code
        )


def check_order_cost(tour, request):
    final_cost = tour.price * len(request.data['passengers'])
    return final_cost == request.data['cost']


def send_mail_(subject, text, recipient="adm.ivm.it@gmail.com"):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, text, email_from, [recipient])


def send_mail_with_html(subject, context, template_name='email/order_success.html', recipient="adm.ivm.it@gmail.com"):
    email_from = settings.EMAIL_HOST_USER
    html_content = render_to_string(template_name, context)
    send_mail(subject, '', email_from, [recipient], html_message=html_content)


def get_phone_info(passenger):
    return f"Номер: {passenger['phone']}'\n" if passenger['phone'] else ''


def generate_successful_email(data):
    passengers_info = "\n\n".join([f"Клієнт №{ind + 1}\n"
                                   f"Імʼя: {passenger['name']} {passenger['surname']}\n"
                                   f"{get_phone_info(passenger)}"
                                   f"Місце: {passenger['place']}" for ind, passenger in enumerate(data['passengers'])])
    return f"Admin, було сформовано нове замовлення\nДеталі замовлення:\n\n" \
           f"Номер замовлення: {data['order_code']}\n" \
           f"Сплачена сума: {data['sumpaid']} грн\n" \
           f"Назва туру: {data['tour']['name']}\n" \
           f"Дати: {data['tour']['date_start']} - {data['tour']['date_end']}\n\n" \
           f"Пасажири:\n{passengers_info}"


def send_payment_error_email(response, payment_status):
    send_mail_(
        subject=f"Помилка оплати - {response.get('order_id')}",
        text=f"Помилка оплати замовлення №{response.get('order_id')}\n\nПомилка: {payment_status}"
    )


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
    passengers = get_passengers_info(order)
    update_tour_free_places(tour, len(passengers))
    tour_data = tour_serializer.data

    return {
        'tour': tour_data,
        'sumpaid': response.get('amount'),
        'order_code': response.get('order_id'),
        'passengers': passengers
    }
