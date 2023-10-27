from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'price_with_currency', 'id')
    list_filter = ('season', 'is_featured', 'date_start', 'status')
    ordering = ['status', 'name']
    search_fields = ['name', 'description']



class TourProgramAdmin(admin.ModelAdmin):
    list_display = ('custom_info', 'name', 'tour_days', 'order', 'id')
    search_fields = ['name']
    list_filter = ['tour_days', 'tour_option', 'tour']


class TourDayAdmin(admin.ModelAdmin):
    list_display = ('day', 'photo')
    ordering = ['day']
    search_fields = ['day']


class AdditionalOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'icon')
    ordering = ['name']
    search_fields = ('name', 'description')
    list_filter = ['tour']

    # def get_icon(self, obj):
    #     return mark_safe(f'<img src={obj.icon} width="50" height="60">')


class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'icon')
    ordering = ['name']
    search_fields = ['name']
    list_filter = ['is_landmark', 'tour']


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ['name']
    search_fields = ['name']


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'aws_url')
    ordering = ['name', 'is_main']
    search_fields = ['name']
    list_filter = ['is_main', 'tour_image']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'surname', 'phone', 'place_number',
                    'verification_code', 'is_primary_contact']
    ordering = ['time_create']
    search_fields = ['name', 'surname', 'phone']
    list_filter = ['is_primary_contact', 'order']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'tour', 'sum_paid', 'time_created']
    ordering = ['time_created']
    search_fields = ['name', 'description']
    list_filter = ['tour']


admin.site.register(Tour, TourAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(AdditionalOption, AdditionalOptionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(TourDay, TourDayAdmin)
admin.site.register(TourDayOption)
admin.site.register(TourProgram, TourProgramAdmin)
admin.site.register(OrderStatus)
