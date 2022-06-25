from django import forms
import django
from django.contrib.auth.forms import AuthenticationForm
from .models import (
    UserAccount,
    Address,
)
from posts.models import Post
from django.utils.text import slugify

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserAccount
        widgets = {
                'username': forms.TextInput(attrs={'class': 'input100' , 'type': 'text', 'placeholder': 'Username'}),
            }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'phone_number',]
       

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'password', 'email', 'phone_number',]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean(self):
        cleand_data = super().clean()
        username = cleand_data.get('username')
        user = UserAccount.objects.filter(username=username)
        if user:
            raise forms.ValidationError('Username already exists')
        return cleand_data


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['district', 'city']

    def save(self, request, commit=True):
        form = super().save(commit=False)
        form.user = request.user
        if commit:
            form.save()
        return form


class UserPostCreation(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'price', 'category']

    def save(self, commit=True):
        form = super().save(commit=False)
        form.slug = slugify(form.title, allow_unicode=True)
        if commit:
            form.save()
        return form