from django.contrib import admin
from .models import *


class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'price_with_currency')
    list_filter = ('season', 'is_featured', 'date_start', 'status')
    ordering = ['status', 'name']
    search_fields = ['name', 'description']


admin.site.register(Tour, TourAdmin)

admin.site.register(Status)
admin.site.register(Season)
admin.site.register(Option)
admin.site.register(Image)
admin.site.register(AdditionalOption)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TourDay)
admin.site.register(TourDayOption)
admin.site.register(TourProgram)
