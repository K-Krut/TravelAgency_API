import random
from django.core.management.base import BaseCommand
from faker import Faker
from travel_api.models import AdditionalOption
from googletrans import Translator


def translate_text(text, src_lang, dest_lang):
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text


fake = Faker()
translator = Translator()


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
    help = 'Update name in AdditionalOption according to '

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, help='Number of fake entries to generate')

    def handle(self, *args, **kwargs):
        num_entries = kwargs['num_entries']
        options_objs = AdditionalOption.objects.all()[:num_entries]
        for option in options_objs:
            name = random.choice(options)
            description = fake.paragraph(random.randint(2, 15))
            option.name = name
            option.name_uk = name
            option.name_ru = translate_text(name, 'uk', 'ru')
            option.description = translate_text(description, 'en_US', 'uk')
            option.description_uk = translate_text(description, 'en_US', 'uk')
            option.description_ru = translate_text(description, 'en_US', 'ru')

            option.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {num_entries}'))
