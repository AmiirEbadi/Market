from django.contrib import admin
from market.posts.models import Category, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', )
    list_filter = ('created_at', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
