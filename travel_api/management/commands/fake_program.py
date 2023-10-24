import random
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import choice

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for MyModel'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']

        for _ in range(num_entries):
            tour = choice(Tour.objects.filter(pk=4))
            day = choice(TourDay.objects.all())
            program_item = TourProgram.objects.filter(tour=tour, tour_days=day).order_by('-order').first()
            order = program_item.order + 1 if program_item and program_item.order else 1
            tour_program = TourProgram.objects.create(
                tour=tour,
                tour_days=day,
                tour_option=choice(TourDayOption.objects.all()),
                order=order
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_entries} fake data entries'))
