from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", null=True, blank=True,)
    slug = models.SlugField(max_length=50, verbose_name="slug", null=True, blank=True,)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name="title", null=True, blank=True)
    slug = models.SlugField(max_length=250, verbose_name="slug", null=False, blank=False, unique=True, allow_unicode=True)
    body = models.TextField(verbose_name="body", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)
    image = models.ImageField(verbose_name="image", null=True, blank=True, upload_to="images")
    price = models.DecimalField(verbose_name="price", max_digits=10, decimal_places=0, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ManyToManyField(
        Category,
        verbose_name="category",
        related_name="posts", 
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name="author",
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'pk' : self.pk})

    def __str__(self) -> str:
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title, allow_unicode=True)
    #     return super().save(*args, **kwargs)
