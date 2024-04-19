from django.shortcuts import render, redirect

from Planet_Discoverers.photos.models import Photo
from Planet_Discoverers.photos.forms import PhotoForm


def add_photo(request):
    form = PhotoForm(request.POST or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()
        return redirect('details_photo', pk=form.instance.pk)

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context=context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')


def delete_photo(request, pk):
    return render(request, 'photos/photo-delete-page.html')

