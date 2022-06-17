from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostsListView(ListView):
    template_name = "post/posts_list.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        list_of_posts = Post.objects.filter(status='published')
        return list_of_posts
