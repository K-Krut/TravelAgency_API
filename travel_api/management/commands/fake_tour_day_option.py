import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
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
           "Страховка",
           "Чани",
           "Заселення",
           "Обід",
           "Виселення",
           "Трансфер",
           "Сироварня",
           "Трансфер до дорагобрату",
           "Пікнік з вершинами",
           "Вечеря",
           "Дорога додому"]


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
            landmark = random.choice([True, False])
            dates = random_dates_within_month(2023, 10)
            url = random.choice(images)
            TourDayOption.objects.create(
                name=random.choice(options),
                description=fake.paragraph(random.randint(0, 15)),
                date_start=dates[0],
                date_end=dates[1],
                is_landmark=landmark,
                image_url=url
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_entries} fake data entries'))
