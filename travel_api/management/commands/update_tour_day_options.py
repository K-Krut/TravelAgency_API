import random
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import TourDayOption
from googletrans import Translator


def translate_text(text, src_lang, dest_lang):
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text


fake = Faker(['uk'])
translator = Translator()


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


class Command(BaseCommand):
    help = 'Update name in TourDayOption according to '

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']
        options_objs = TourDayOption.objects.all()[:num_entries]
        for option in options_objs:
            name = random.choice(options)
            description = fake.paragraph(random.randint(2, 15))
            option.name = name
            option.name_uk = name
            option.name_ru = translate_text(name, 'uk', 'ru')
            option.description = description
            option.description_uk = description
            option.description_ru = translate_text(description, 'uk', 'ru')

            option.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {num_entries}'))
