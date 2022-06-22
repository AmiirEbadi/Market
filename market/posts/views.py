from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView
)
from .models import (
    Category,
    Post,
)


class PostsListView(ListView):
    template_name = "post/posts_list.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        list_of_posts = Post.objects.filter(status='published')
        return list_of_posts


class PostDetailView(DetailView):
    template_name = "post/post_detail.html"
    context_object_name = 'post'

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post

    def get_context_data(self, **kwargs):
        """ here i get last 4 posts that have the same category with this post """

        context = super().get_context_data(**kwargs)
        post_categories = [category.id for category in context['object'].category.all()]
        related_posts = Post.objects.filter(category__id__in = post_categories).distinct()
        context['related_posts'] = related_posts[:4]
        return context


class PostsCategoryListView(ListView):
    template_name = "post/posts_category_list.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        list_of_posts = category.posts.filter(status='published')
        return list_of_posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context