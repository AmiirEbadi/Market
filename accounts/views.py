from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
)
from .forms import(
    UserLoginForm,
    UserProfileForm,
    UserSignUpForm,
    UserAddressForm,
    UserPostCreation,
)

from .models import (
    UserAccount,
    Address,
)

from posts.models import Post
from django.views.generic.base import View
from django.views.generic.edit import DeleteView
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
            user = signup_form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('account:signin')

        errors = signup_form.non_field_errors
        signup_form = UserSignUpForm()
        return render(request, 'account/signup.html', {'signup_form': signup_form , 'errors': errors})

    def get(self, request, *args, **kwargs):
        signup_form = UserSignUpForm()
        return render(request, 'account/signup.html', {'signup_form': signup_form})



class UserProfileView(LoginRequiredMixin, View):
    ''' This View is used to update the user profile also user can see his info here '''

    def get(self, request, *args, **kwargs):
        user_address = Address.objects.filter(user=request.user).first()
        profile_form = UserProfileForm(instance=request.user)
        address_form = UserAddressForm(instance=user_address)
        context = {
            'profile_form': profile_form,
            'address_form': address_form,
        }
        return render(request, 'account/profile.html', context=context)

    def post(self, request, *args, **kwargs):
        if 'profile' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                return self.get(request, *args, **kwargs)
        elif 'address' in request.POST:
            user_address = Address.objects.filter(user=request.user).first()
            address_form = UserAddressForm(request.POST, instance=user_address)
            if address_form.is_valid():
                address_form.save(request)
                return self.get(request, *args, **kwargs)


class UserPostCreationView(LoginRequiredMixin, View):
    ''' This View is used to create a post '''

    def get(self, request, *args, **kwargs):
        post_form = UserPostCreation()
        user_posts = Post.objects.filter(author=request.user)
        context = {
            'post_form': post_form,
            'user_posts': user_posts,
        }
        return render(request, 'account/post_create.html', context=context)

    def post(self, request, *args, **kwargs):
        post_form = UserPostCreation(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
        return HttpResponse('Post created')


class UserPostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('account:profile')
    template_name = 'account/post_delete_confirm.html'