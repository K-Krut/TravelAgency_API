import random
import ssl

from django.shortcuts import redirect
from rest_framework.views import exception_handler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from TravelAgency_API import settings
from liqpayapi.liqpay3 import LiqPay
from .models import *
from django.core.mail import send_mail
import smtplib


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


def create_order(order, place_number, name, surname, phone, price, is_primary_contact, code):
    print(phone, is_primary_contact)

    if is_primary_contact is None and phone is None:
        OrderItem.objects.create(
            order=order,
            place_number=place_number,
            name=name,
            surname=surname,
            phone="None",
            sum=price,
            is_primary_contact=False,
            verification_code=code
        )
    else:
        OrderItem.objects.create(
            order=order,
            place_number=place_number,
            name=name,
            surname=surname,
            phone=phone,
            sum=price,
            is_primary_contact=is_primary_contact,
            verification_code=code
        )


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


def send_mail_(subject, text, recipient="adm.ivm.it@gmail.com"):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, text, email_from, [recipient])


def create_message(order, sumpaid):
    message = "Admin, було сформовано нове замовлення\nДеталі замовлення"

    message = message + f"\nНомер замовлення: {order.code}"
    message = message + f"\nСплачена сума: {sumpaid} грн"
    message = message + f"Назва туру: {order.tour.name}\n\nДата початку: {order.tour.date_start}\n\nДата Кінця: {order.tour.date_end}"
    message = message + "\n\nПасажири"

    items = OrderItem.objects.filter(order=order)

    print(items)

    for item in items:
        message = message + f"\n\nІмʼя: {item.name} {item.surnamename}\nНомер: {item.phone}\nМісце: {item.place_number}"

    print(message)
    return message


def send_payment_error_email(response, payment_status):
    send_mail_(
        subject=f"Помилка оплати - {response.get('order_id')}",
        text=f"Помилка оплати замовлення №{response.get('order_id')}\n\nПомилка: {payment_status}"
    )

def get_tour_info_for_order(order, response):
    tour = Tour.objects.get(pk=order.tour.pk)
    free_places = tour.free_places - len(OrderItem.objects.filter(order=order))
    print(order.tour)
    print(tour)
    print(tour.id)

    return {
        'tour': {
            'id': tour.id,
            'name': tour.name,
            'date_start': tour.date_start,
            'date_end': tour.date_end,
            'price': tour.price,
            'free_places': free_places,
            'season': tour.season,
            'images': [img.aws_url for img in Image.objects.filter(tour_image=tour)]
        },
        'sumpaid': response.get('amount'),
        'order_code': response.get('order_id')
    }
