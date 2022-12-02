from django.contrib import admin
from django.urls import path
from .views import (
    PostsListView,
    PostDetailView,
    PostsCategoryListView
)

app_name = 'posts'
urlpatterns = [
    path('all/', PostsListView.as_view(), name='all-posts'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('category/<slug:slug>', PostsCategoryListView.as_view(), name="category-posts"),
]