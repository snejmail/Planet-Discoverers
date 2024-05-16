from django.contrib import admin
from django.urls import path, include

from Planet_Discoverers.common.views import index, custom_404_view
from Planet_Discoverers.planets.views import planet_search

urlpatterns = (
    path('', index, name='index'),
    path('search/', planet_search, name='planet_search'),
    path('404/', custom_404_view, name='404'),
)
