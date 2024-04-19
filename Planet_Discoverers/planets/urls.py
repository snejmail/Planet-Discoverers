from django.contrib import admin
from django.urls import path, include

from Planet_Discoverers.planets.views import add_planet, details_planet, edit_planet, delete_planet, planet_search

urlpatterns = (
    path('add/', add_planet, name='add_planet'),
    path('<int:pk>/', include([
        path('', details_planet, name='details_planet'),
        path('edit/', edit_planet, name='edit_planet'),
        path('delete/', delete_planet, name='delete_planet'),
    ]))
)

