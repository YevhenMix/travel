from django.contrib import admin
from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
