from modeltranslation.translator import TranslationOptions, register
from .models import Tour, Option, AdditionalOption, TourDayOption


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(AdditionalOption)
class OptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



@register(TourDayOption)
class OptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

