from django.shortcuts import render, redirect, get_object_or_404

from Planet_Discoverers.photos.models import Photo
from Planet_Discoverers.photos.forms import PhotoForm


def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST or None)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('details_photo', pk=form.instance.pk)

    else:
        form = PhotoForm()

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details_photo', pk=pk)
    else:
        form = PhotoForm(instance=photo)

    context = {
        'photo': photo,
        'form': form,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == "POST":
        photo.delete()
        return redirect('details_photo', pk=pk)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo-delete-page.html', context)

