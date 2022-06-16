from django.contrib import admin
from django.urls import path
from .views import PostsListView

urlpatterns = [
    path('all/', PostsListView.as_view()),
]