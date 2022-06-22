from webbrowser import get
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.contrib.auth.views import (
    LoginView,
    
)
from .forms import(
    UserLoginForm,
    UserProfileForm,
    UserSignUpForm,
)

from .models import UserAccount
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserSignInView(LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse('account:profile')


class UserSignUpView(View):
    def post(self, request, *args, **kwargs):
        signup_form = UserSignUpForm(request.POST)
        if signup_form.is_valid():
            # username = signup_form.cleaned_data['username']
            # password = signup_form.cleaned_data['password']
            # UserAccount.objects.create_user(username, password)
            user = signup_form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('account:signin')
        x = signup_form.non_field_errors
        print([i for i in signup_form.errors])
        signup_form = UserSignUpForm()
        return render(request, 'account/signup.html', {'signup_form': signup_form , 'x': x})

    def get(self, request, *args, **kwargs):
        signup_form = UserSignUpForm()
        return render(request, 'account/signup.html', {'signup_form': signup_form})



class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        profile_form = UserProfileForm(instance=request.user)
        context = {
            'form': profile_form,
        }
        return render(request, 'account/profile.html', context=context)

    def post(self, request, *args, **kwargs):
        profile_form = UserProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return self.get(request, *args, **kwargs)
