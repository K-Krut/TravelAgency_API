import random
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import Option, Tour
from .data.additional_options_images import images

fake = Faker()

icons = [
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/bed.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/breakfast.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/bus.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/camera.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/cheese.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/guide.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/man.svg',
    'https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/other.svg',
]
options = ["Переїзд",
           "Сніданок в готелі",
           "Проживання",
           "Супровід гіда протягом всього туру",
           "Фотозвіт",
           "Харчування",
           "Екскурсійна програма",
           "Спортивне спорядження",
           "Страховка"]


class Command(BaseCommand):
    help = 'Generate fake data for MyModel'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']

        for _ in range(num_entries):
            landmark = random.choice([True, False])
            url = random.choice(images) if landmark else None
            option = Option.objects.create(
                name=random.choice(options),
                is_landmark=landmark,
                icon=random.choice(icons),
                image_url=url
            )
            for _ in range(random.randint(0, 10)):
                option.tour.add(random.choice(Tour.objects.all()))
            # option = Option.objects.get(pk=random.randint(54, 85))
            # for _ in range(random.randint(0, 10)):
            #     option.tour.add(random.choice(Tour.objects.all()))

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_entries} fake data entries'))
