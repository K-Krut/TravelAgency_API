import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import randint

fake = Faker()


def random_dates_within_month(year, month):
    end_date = datetime(year + 1, 1, 1) - timedelta(days=1) if month == 12 else datetime(year, month + 1,
                                                                                         1) - timedelta(days=1)
    start = fake.date_between_dates(datetime(year, month, 1), end_date.date())
    end = start + timedelta(days=random.choice([3, 4, 5, 7]))
    return start, end


class Command(BaseCommand):
    help = 'Generate fake data for MyModel'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']

        for _ in range(num_entries):
            place = randint(25, 100)
            dates = random_dates_within_month(2023, 10)
            Tour.objects.create(
                name=fake.city(),
                description=fake.paragraph(randint(0, 15)),
                price=randint(1000, 10000),
                places=place,
                free_places=place - randint(0, place),
                is_featured=random.choice([True, False]),
                date_start=dates[0],
                date_end=dates[1],
                status=random.choice(Status.objects.all()),
                season=random.choice(Season.objects.all())
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_entries} fake data entries'))
