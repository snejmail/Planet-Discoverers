from django.contrib import admin

from Planet_Discoverers.planets.models import Planet


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

