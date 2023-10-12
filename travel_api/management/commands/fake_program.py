import random
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from .data.additional_options_images import images

fake = Faker()


class Command(BaseCommand):
    help = 'Generate fake data for MyModel'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']

        all_tours = list(Tour.objects.all())
        all_tour_days = list(TourDay.objects.all())
        all_tour_day_options = list(TourDayOption.objects.all())

        for _ in range(num_entries):
            selected_tours = random.sample(all_tours, k=random.randint(1, len(all_tours)))
            selected_tour_days = random.sample(all_tour_days, k=random.randint(1, len(all_tour_days)))
            selected_tour_day_options = random.sample(all_tour_day_options,
                                                      k=random.randint(1, len(all_tour_day_options)))

            tour_program = TourProgram.objects.create()

            tour_program.tour.set(selected_tours)
            tour_program.tour_day.set(selected_tour_days)
            tour_program.tour_option.set(selected_tour_day_options)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_entries} fake data entries'))
