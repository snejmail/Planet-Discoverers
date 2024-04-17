from django.shortcuts import render, redirect

from Planet_Discoverers.photos.models import Photo
from Planet_Discoverers.planets.forms import PlanetForm, PlanetSearchForm
from Planet_Discoverers.planets.models import Planet


def get_planet_by_id(planet_id):
    return Planet.objects.get(pk=planet_id)


def add_planet(request):
    form = PlanetForm(request.POST or None)
    if form.is_valid():
        planet = form.save(commit=False)
        planet.user = request.user
        planet.save()
        return redirect('details_planet', pk=form.instance.pk)

    context = {
        'form': form,
    }

    return render(request, 'planets/planet-add-page.html', context=context)


def details_planet(request, pk):
    planet = get_planet_by_id(pk)
    all_photos = planet.planet_photos.all()

    context = {
        'planet': planet,
        'all_photos': all_photos,
    }

    return render(request, 'planets/planet-details-page.html', context)


def edit_planet(request, pk):
    planet = get_planet_by_id(pk)

    if request.method == 'POST':
        form = PlanetForm(request.POST, instance=planet)
        if form.is_valid():
            form.save()
    else:
        form = PlanetForm(instance=planet)

    context = {
        'form': form,
        'planet': planet,
    }
    return render(request, 'planets/planet-edit-page.html', context)


def delete_planet(request, pk):
    planet = get_planet_by_id(pk)

    if request.method == 'POST':
        planet.delete()
        return redirect('index')

    context = {
        'planet': planet,
    }

    return render(request, 'planets/planet-delete-page.html', context)


def planet_search(request):
    form = PlanetSearchForm(request.GET)
    query = request.GET.get('search_query')
    planets = []

    if query:
        planets = Planet.objects.filter(name__icontains=query)
    else:
        return "No planets found"

    context = {
        'form': form,
        'planets': planets,
        'query': query,
    }

    return render(request, 'planets/planet_search.html', context)

