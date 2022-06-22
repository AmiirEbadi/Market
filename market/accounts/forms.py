from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount


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

    def clean_username(self):
        username = self.data.get('username')
        user = UserAccount.objects.filter(username=username)
        if user:
            raise forms.ValidationError('Username already exists')
        return username