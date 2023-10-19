import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import randint
from .data.images import images
from django.db.utils import IntegrityError
fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for Images'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        a = ''
        queryset = Tour.objects.filter()
        for _ in range(kwargs['num_entries']):
            try:
                choice_image = random.choice(queryset)
                if choice_image == a:
                    pass
                else:
                    img = Image.objects.create(
                        name="image.png",
                        aws_url=random.choice(images),
                        is_main=random.choice([True, False, False, False, False, False, False, False, False])
                    )
                    img.tour_image.add(choice_image)
                    a = choice_image
            except IntegrityError:
                continue

        self.stdout.write(self.style.SUCCESS(f'Successfully generated fake data entries'))
