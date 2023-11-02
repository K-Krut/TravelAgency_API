from modeltranslation.translator import TranslationOptions, register
from .models import Tour, Option, AdditionalOption


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('name', )



@register(AdditionalOption)
class OptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

