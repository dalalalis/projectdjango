from django.contrib import admin
from .models import Events
# Register your models here.
@admin.register(Events)
class EventsAdmin (admin.ModelAdmin):
    list_display=("","","", "",)
    list_display_links= ("", "",)
    list_filter= ("active",)
