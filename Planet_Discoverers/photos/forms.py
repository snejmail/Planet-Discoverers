from django.forms import ModelForm

from Planet_Discoverers.photos.models import Photo


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'
