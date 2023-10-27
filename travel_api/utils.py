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


def send_mail_(to_addr, subject, text):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, text, email_from, [to_addr])


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


def update_order(response):
    order = Order.objects.get(code=response.get('order_id'))
    order.status = OrderStatus.objects.get(id=4)
    order.sum_paid = int(response.get('amount')) if response.get('amount') else 0
    order.paytype = response.get('paytype')
    order.sender_card_mask_2 = response.get('sender_card_mask2')
    order.receiver_commission = response.get('receiver_commission')
    order.save()
    return order


