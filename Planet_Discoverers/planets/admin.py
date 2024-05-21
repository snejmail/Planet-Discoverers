from django.contrib import admin

from Planet_Discoverers.planets.models import Planet


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'discoverer')
    list_filter = ('type', 'in_habitable_zone')
    search_fields = ('name', 'type', 'discoverer')
    ordering = ('name',)
    actions = ['flag_as_duplicate']

    def flag_as_duplicate(self, request, queryset):
        for planet in queryset:
            planet.is_duplicate = True
            planet.save()
    flag_as_duplicate.short_description = "Flag selected planets as duplicate"

