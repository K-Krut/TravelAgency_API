import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import randint
from .data.images import images
fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for Images'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        for _ in range(kwargs['num_entries']):
            Image.objects.create(
                # tour_image=Tour.objects.get(pk=192),
                tour_image=random.choice(Tour.objects.all()),
                aws_url=random.choice(images),
                is_main=random.choice([True, False, False, False, False, False, False, False, False])
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated fake data entries'))
