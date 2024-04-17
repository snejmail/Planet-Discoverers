from django import forms

from Planet_Discoverers.photos.models import Photo
from Planet_Discoverers.planets.models import Planet


# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ['photo', 'description']


class PlanetForm(forms.ModelForm):

    class Meta:
        model = Planet
        fields = '__all__'


class PlanetSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for planet here...',
        })
    )


