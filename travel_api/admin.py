from django.contrib import admin
from .models import *


class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'price_with_currency', 'id')
    list_filter = ('season', 'is_featured', 'date_start', 'status')
    ordering = ['status', 'name']
    search_fields = ['name', 'description']



class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')



admin.site.register(Tour, TourAdmin)

admin.site.register(Status)
admin.site.register(Season)
admin.site.register(Option, OptionAdmin)
admin.site.register(Image)
admin.site.register(AdditionalOption)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TourDay)
admin.site.register(TourDayOption)
admin.site.register(TourProgram)
