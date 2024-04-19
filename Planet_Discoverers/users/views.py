from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views

from Planet_Discoverers.users.forms import UserRegisterForm, UserLoginForm, UserEditForm, UserDeleteForm
from Planet_Discoverers.users.models import User


class UserRegisterView(views.CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register-page.html'
    success_url = reverse_lazy('login_user')


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'users/login-page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login_user')


class UserEditView(views.UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('edit_user', kwargs={'pk': self.object.pk})


def details_user(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
    }

    return render(request, 'users/profile-details-page.html', context)


def delete_user(request, pk):
    profile = User.objects.first()
    form = UserDeleteForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'users/profile-delete-page.html', context)
