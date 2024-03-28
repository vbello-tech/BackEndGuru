from django import forms
from .models import UserProfile, User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CreateProfileForm(forms.Form):
    bio = forms.CharField(required=True)
    image = forms.ImageField(required=False)
    stack = forms.CharField(required=True)
    github = forms.URLField(required=True)
    twitter = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    other = forms.URLField(required=False)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'EMAIL ADDRESS',
        'class': 'form-control',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'PASSWORD',
    }))


