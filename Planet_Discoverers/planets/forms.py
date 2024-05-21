from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from Planet_Discoverers.users.models import User
from django.forms import ModelForm
from django import forms

from Planet_Discoverers.planets.models import Planet, Photo


class PlanetForm(forms.ModelForm):

    class Meta:
        model = Planet
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        finding_method = cleaned_data.get('finding_method')
        primary_photo = cleaned_data.get('primary_photo')
        if finding_method == 'Direct Imaging' and not primary_photo:
            raise ValidationError("Photo must be provided for planets found through direct imaging.")


class PlanetSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for planet here...',
        })
    )


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['image_upload']


class PhotoUploadForm(forms.Form):
    photo = forms.FileField(label='Select a photo')


class UserRegistrationForm(UserCreationForm):
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'photo']
