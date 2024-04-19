from django import forms

from Planet_Discoverers.planets.models import Planet


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


