from django.contrib import admin

from Planet_Discoverers.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication')


