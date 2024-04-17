from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from Planet_Discoverers.users.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture', 'country')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:
            if password1:
                raise error
        return password1

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in ['username', 'email', 'password1', 'password2']:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        for field_name in self.fields:
            self.fields[field_name].help_text = ''


class UserLoginForm(AuthenticationForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserLoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({
    #         'class': 'form-control'
    #     })
    #     self.fields['password'].widget.attrs.update({
    #         'class': 'form-control'
    #     })

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        )


class UserEditForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'profile_picture', 'country')
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'email': 'Email',
            'profile_picture': 'Profile picture',
            'country': 'Country',
        }


class UserDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = User
        fields = ()
