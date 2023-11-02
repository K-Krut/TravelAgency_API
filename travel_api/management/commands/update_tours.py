import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import *
from random import randint
from googletrans import Translator


def translate_text(text, src_lang, dest_lang):
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text


fake = Faker()
translator = Translator()


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
        tours = Tour.objects.all()[:num_entries]
        for tour in tours:
            city = fake.city()
            description = fake.paragraph(randint(4, 15))

            tour.name = translate_text(city, 'en_US', 'uk')
            tour.name_uk = translate_text(city, 'en_US', 'uk')
            tour.name_ru = translate_text(city, 'en_US', 'ru')
            tour.description = translate_text(description, 'en_US', 'uk')
            tour.description_uk = translate_text(description, 'en_US', 'uk')
            tour.description_ru = translate_text(description, 'en_US', 'ru')

            tour.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {num_entries}'))
