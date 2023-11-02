from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.safestring import mark_safe
from django.utils import formats
from .models import *


class TourAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'formatted_date_start', 'formatted_date_end', 'price_with_currency', 'get_image', 'id')
    list_filter = ('season', 'is_featured', 'date_start', 'status')
    ordering = ['status', 'name']
    search_fields = ['name', 'description']

    def formatted_date_start(self, obj):
        return formats.date_format(obj.date_start, "Y-m-d")
    formatted_date_start.short_description = 'Дата початку'

    def formatted_date_end(self, obj):
        return formats.date_format(obj.date_end, "Y-m-d")
    formatted_date_end.short_description = 'Дата кінця'

    def get_image(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        image = main_image.aws_url if main_image else None
        return mark_safe(f'<a href="{image}" target="_blank">'
                         f'<img src="{image}" width=auto height="100"></a>') if image else None

    get_image.short_description = 'Зображення'


class TourProgramAdmin(admin.ModelAdmin):
    list_display = ('custom_info', 'name', 'tour_days', 'is_landmark', 'get_image_url', 'order')
    search_fields = ['name']
    list_filter = ['is_landmark', 'tour_days', 'tour_option', 'tour']

    def get_image_url(self, obj):
        return mark_safe(f'<a href="{obj.image_url}" target="_blank">'
                         f'<img src="{obj.image_url}" width=auto height="120"></a>') if obj.image_url else None

    get_image_url.short_description = 'Зображення'



class TourDayAdmin(admin.ModelAdmin):
    list_display = ('day', 'photo')
    ordering = ['day']
    search_fields = ['day']


class AdditionalOptionAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'price', 'get_icon')
    ordering = ['name']
    search_fields = ('name', 'description')
    list_filter = ['tour']

    def get_icon(self, obj):
        return mark_safe(f'<a href="{obj.icon}" target="_blank">'
                         f'<img src="{obj.icon}" width=auto height="60">') if obj.icon else None

    get_icon.short_description = 'Icon'


class OptionAdmin(TabbedTranslationAdmin):
    exclude = ['is_landmark', 'image_url']
    list_display = ('name', 'get_icon')
    ordering = ['name']
    search_fields = ['name']
    list_filter = ['tour']

    def get_icon(self, obj):
        return mark_safe(f'<a href="{obj.icon}" target="_blank">'
                         f'<img src="{obj.icon}" width=auto height="60">') if obj.icon else None

    get_icon.short_description = 'Icon'



class TourDayOptionAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'is_landmark', 'get_image_url')
    ordering = ['name']
    search_fields = ['name']
    list_filter = ['is_landmark', 'date_start']

    def get_image_url(self, obj):
        return mark_safe(f'<a href="{obj.image_url}" target="_blank">'
                         f'<img src="{obj.image_url}" width=auto height="60">') if obj.image_url else None

    get_image_url.short_description = 'Зображення'


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ['name']
    search_fields = ['name']


class SeasonAdmin(TabbedTranslationAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'get_aws_image')
    ordering = ['name', 'is_main']
    search_fields = ['name']
    list_filter = ['is_main', 'tour_image']

    def get_aws_image(self, obj):
        return mark_safe(f'<a href="{obj.aws_url}" target="_blank">'
                         f'<img src="{obj.aws_url}" width=auto height="120"></a>') if obj.aws_url else None

    get_aws_image.short_description = 'Зображення'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'surname', 'phone', 'place_number',
                    'verification_code', 'is_primary_contact']
    ordering = ['time_create']
    search_fields = ['name', 'surname', 'phone']
    list_filter = ['is_primary_contact', 'order']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'tour', 'status', 'sum_paid', 'paytype', 'receiver_commission', 'time_created']
    ordering = ['status', '-time_created']
    search_fields = ['name', 'description']
    list_filter = ['status', 'time_created', 'paytype', 'tour']


admin.site.register(Tour, TourAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(AdditionalOption, AdditionalOptionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(TourDay, TourDayAdmin)
admin.site.register(TourDayOption, TourDayOptionAdmin)
admin.site.register(TourProgram, TourProgramAdmin)
admin.site.register(OrderStatus)
