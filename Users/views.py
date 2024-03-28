from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from .forms import CreateProfileForm, NewUserForm, LoginForm
from .models import UserProfile, User
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from Challenges.models import Challenge


# Create your views here.


def home(request):
    challenge = Challenge.objects.order_by('-created_date')[:3]
    return render(request, 'home.html', {'challenges': challenge})


# sign up
def signup_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            subject = 'Subject'
            html_message = render_to_string('account/signup_email.html', {'context': user.username})
            plain_message = strip_tags(html_message)
            mail.send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [user.email], html_message=html_message)
            return redirect('/')
    else:
        form = NewUserForm()

    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)


# login
class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(self.request, 'account/login.html', context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, email=email, password=password)
            if user:
                auth.login(self.request, user)
                messages.success(self.request, "Account login successful.")
                return redirect('/')
            elif not User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.info(self.request, "You dont have an account. Kindly signup.")
                return redirect('user:signup')
            else:
                messages.info(self.request, "Email or password incorrect.")
                return redirect('user:login')
        else:
            return redirect('user:login')


# logout
class LogoutView(View, LoginRequiredMixin):
    def get(self, *args, **kwargs):
        auth.logout(self.request)
        messages.success(self.request, "Account logout successful.")
        return HttpResponseRedirect('/')


# change password
class ChangePasswordView(View, LoginRequiredMixin):
    def get(self, *args, **kwargs):
        form = PasswordChangeForm(user=self.request.user)
        context = {
            'form': form
        }
        return render(self.request, 'account/change_password.html', context)

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            form = PasswordChangeForm(data=self.request.POST, user=self.request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(self.request, form.user)
                return redirect('/')
        else:
            form = PasswordChangeForm(user=self.request.user)


# create profile
class CreateProfileView(View, LoginRequiredMixin):
    def get(self, *args, **kwargs):
        form = CreateProfileForm()
        context = {
            'form': form,
        }
        return render(self.request, 'account/createprofile.html', context)

    def post(self, *args, **kwargs):
        form = CreateProfileForm(self.request.POST, self.request.FILES)
        profile = get_object_or_404(UserProfile, user=self.request.user)
        if form.is_valid():
            profile.bio = form.cleaned_data.get('bio'),
            profile.image = form.cleaned_data.get('image'),
            profile.stack = form.cleaned_data.get('stack'),
            profile.github = form.cleaned_data.get('github'),
            profile.twitter = form.cleaned_data.get('twitter'),
            profile.linkedin = form.cleaned_data.get('linkedin'),
            profile.other = form.cleaned_data.get('other')
            profile.save()
            return redirect(profile.get_profile())
        else:
            form = CreateProfileForm()


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'account/profile.html', {
            'profile': UserProfile.objects.get(user=request.user),
        })
