from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    UserSignInView,
    UserProfileView,
    UserSignUpView,
)

app_name = 'account'
urlpatterns = [
    path('signin/', UserSignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('signup/', UserSignUpView.as_view(), name='signup'),

    path('profile/', UserProfileView.as_view(), name='profile'),
]