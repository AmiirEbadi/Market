from pyexpat import model
from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="title",
        null=True,
        blank=True,
        )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="title",
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=250,
        verbose_name="slug",
        null=False,
        blank=False,
        unique=True,
    )
    body = models.TextChoices(
        verbose_name="title",
        null=True,
        blank=True,
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="category",
        related_name="posts", 
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name="author",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name="created at",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="updated at",
        auto_now=True,
    )
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self) -> str:
        return self.title


