from rest_framework.views import exception_handler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import *

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


def send_mail(to_addr, subject, text):
    msg = MIMEMultipart()

    msg['From'] = "grachuxas@yandex.ru"
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(
        MIMEText(text, 'plain')
    )

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo('grachuxas@yandex.ru')
    server.login('grachuxas@yandex.ru', 'dagos527563')
    server.auth_plain()
    server.send_message(msg)
    server.quit()


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