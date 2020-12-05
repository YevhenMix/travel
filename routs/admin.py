from django.contrib import admin

from routs.models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
