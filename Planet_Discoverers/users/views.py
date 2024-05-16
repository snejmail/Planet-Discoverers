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


class CustomLoginView(auth_views.LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'users/login-page.html'
    # next_page = reverse_lazy('index')
    success_url = reverse_lazy('email_greeting')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login_user')


class UserEditView(views.UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('details_user', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if 'profile_picture' in self.request.FILES:
            profile_picture = self.request.FILES['profile_picture']
            self.object.profile_picture = profile_picture
        return super().form_valid(form)


def details_user(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
    }

    return render(request, 'users/profile-details-page.html', context)


def delete_user(request, pk):
    user = User.objects.first()
    form = UserDeleteForm(instance=user)

    if request.method == 'POST':
        user.delete()
        return redirect('index')

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'users/profile-delete-page.html', context)


def email_greeting(request):
    context = {
        'user': request.user
    }
    return render(request, 'email-greeting.html', context)
