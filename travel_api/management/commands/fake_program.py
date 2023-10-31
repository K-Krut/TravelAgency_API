import random
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import choice
from .data.additional_options_images import images

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for MyModel'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']

        for _ in range(num_entries):
            tour = choice(Tour.objects.all())
            # tour = choice(Tour.objects.filter(pk=1))
            day = choice(TourDay.objects.all())
            program_item = TourProgram.objects.filter(tour=tour, tour_days=day).order_by('-order').first()
            order = program_item.order + 1 if program_item and program_item.order else 1
            landmark = True
            # landmark = random.choice([True, False])
            url = random.choice(images) if landmark else None

            tour_program = TourProgram.objects.create(
                tour=tour,
                tour_days=day,
                tour_option=choice(TourDayOption.objects.all()),
                order=order,
                is_landmark=landmark,
                image_url=url
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_entries} fake data entries'))
