from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Planet_Discoverers.planets.forms import PlanetForm, PlanetSearchForm, PhotoForm
from Planet_Discoverers.planets.models import Planet, Photo


def get_planet_by_id(planet_id):
    return Planet.objects.get(pk=planet_id)


@login_required
def add_planet(request):
    if request.method == 'POST':
        form = PlanetForm(request.POST, request.FILES)
        if form.is_valid():
            planet = form.save(commit=False)
            photo_file = request.FILES.get('photo')
            if photo_file:
                Photo.objects.create(planet=planet, image_upload=photo_file)
            planet.discoverer = request.user
            planet.save()
            return redirect('details_planet', pk=planet.pk)
    else:
        form = PlanetForm()

    context = {
        'form': form,
    }

    return render(request, 'planets/planet-add-page.html', context)


def details_planet(request, pk):
    planet = get_object_or_404(Planet, pk=pk)
    all_photos = planet.photos.all()

    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo = photo_form.save(commit=False)
            photo.planet = planet
            photo.save()
            return redirect('details_planet', pk=pk)
    else:
        photo_form = PhotoForm()

    context = {
        'planet': planet,
        'primary_photo': planet.primary_photo,
        'all_photos': all_photos,
        'photo_form': photo_form,
    }

    return render(request, 'planets/planet-details-page.html', context)


def edit_planet(request, pk):
    planet = get_planet_by_id(pk)

    if request.method == 'POST':
        form = PlanetForm(request.POST, request.FILES, instance=planet)
        if form.is_valid():
            form.save()
            return redirect('details_planet', pk=planet.pk)
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
        return render(request, 'planets/no-results.html')

    context = {
        'form': form,
        'planets': planets,
        'query': query,
    }

    return render(request, 'planets/planet-search.html', context)


def add_photo(request, pk):
    planet = get_object_or_404(Planet, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.planet = planet
            photo.save()
            return redirect('details_planet', pk=pk)

    else:
        form = PhotoForm()

    context = {
        'form': form,
        'planet': planet,
    }

    return render(request, 'photos/photo-add-page.html', context)


# @login_required
# def edit_photo(request, pk):
#     photo = get_object_or_404(Photo, pk=pk)
#     planet_id = photo.planet.pk
#
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES, instance=photo)
#         if form.is_valid():
#             form.save()
#             return redirect('details_planet', pk=planet_id)
#     else:
#         form = PhotoForm(instance=photo)
#
#     context = {
#         'photo': photo,
#         'form': form,
#     }
#
#     return render(request, 'photos/photo-edit-page.html', context)
#

@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    planet_id = photo.planet.pk

    if request.method == "POST":
        photo.delete()
        return redirect('details_planet', pk=planet_id)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo-delete-page.html', context)


@login_required
def catalogue(request):
    user = request.user
    user_planets = Planet.objects.filter(discoverer=user)
    context = {
        'user_planets': user_planets,
    }
    return render(request, 'planets/catalogue.html', context)

