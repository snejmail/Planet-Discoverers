from django.contrib import admin
from django.urls import path, include

from Planet_Discoverers.photos.views import add_photo, details_photo, edit_photo, delete_photo

urlpatterns = (
    path('add/', add_photo, name='add_photo'),
    path('<int:pk>/', include([
         path('', details_photo, name='details_photo'),
         path('edit/', edit_photo, name='edit_photo'),
         path('delete/', delete_photo, name='delete_photo'),
    ]))
)

