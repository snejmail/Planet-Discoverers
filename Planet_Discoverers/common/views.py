from django.shortcuts import render

from Planet_Discoverers.planets.forms import PlanetSearchForm


def index(request):
    search_form = PlanetSearchForm()

    context = {
        'search_form': search_form,
    }

    return render(request, 'base/home-page.html', context)