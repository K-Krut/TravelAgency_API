import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from .data.additional_options_images import images

fake = Faker()


class Command(BaseCommand):
    help = 'Генерация Order Status'

    def handle(self, *args, **kwargs):
        status = [
            {
                'name': 'error',
                'description': 'Data is incorrect'
            },
            {
                'name': 'fallure',
                'description': 'Failed payment'
            },
            {
                'name': 'reversed',
                'description': 'Payment refunded'
            },
            {
                'name': 'success',
                'description': 'Successful payment'
            },
            {
                'name': '3ds_verify',
                'description': '3ds verification is required. To finish the payment you will require a 3ds_verify'
            },
            {
                'name': 'cvv_verify',
                'description': "Sender's card CVV is required."
            },
            {
                'name': 'otp_verify',
                'description': 'OTP Confirmation is required.'
            },
            {
                'name': 'receiver_verify',
                'description': 'Receiver additional data is required'
            },
            {
                'name': 'sender verify',
                'description': 'Sender additional data is required'
            }
        ]

        for data in status:
            OrderStatus.objects.create(
                status=data['name'],
                description=data['description']
            )

        self.stdout.write(self.style.SUCCESS(f'Успех'))
