from django.contrib import admin
from django.urls import path, include

from Planet_Discoverers.common.views import index
from Planet_Discoverers.planets.views import planet_search

urlpatterns = (
    path('', index, name='index'),
    path('search/', planet_search, name='planet_search'),

)
