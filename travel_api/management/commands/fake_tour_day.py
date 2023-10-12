import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import randint

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for TourDay'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']

        for i in range(num_entries):
            TourDay.objects.create(
                day=i + 1
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated fake data entries'))
