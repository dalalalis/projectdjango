from django.contrib import admin
from .models import EventItem
# Register your models here.
admin.site.register(EventItem)

#class EventsAdmin (admin.ModelAdmin):
    #list_display=("","","", "",)
    #list_display_links= ("", "",)
    #list_filter= ("active",)
