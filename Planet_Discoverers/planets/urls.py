from django.contrib import admin
from django.urls import path, include

from Planet_Discoverers.planets.views import add_planet, details_planet, edit_planet, delete_planet, add_photo, \
    delete_photo, catalogue

urlpatterns = (
    path('catalogue/', catalogue, name='catalogue'),
    path('add/', add_planet, name='add_planet'),
    path('photos/', include([
        path('<int:pk>/', include([
                # path('edit/', edit_photo, name='edit_photo'),
                path('delete/', delete_photo, name='delete_photo')
            ]))
        ])),
    path('<int:pk>/', include([
        path('', details_planet, name='details_planet'),
        path('edit/', edit_planet, name='edit_planet'),
        path('delete/', delete_planet, name='delete_planet'),
        path('add-photo/', add_photo, name='add_photo'),
    ])),
)
