from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify 

# Create your models here.

class PostCategory(models.Model):
    category = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Post Categories")
        verbose_name_plural = ("Post Categories")
        ordering = ("-timestamp",)

    def __str__(self):
        return self.category


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    post_image = models.ImageField(upload_to="post/images")
    post_content = RichTextField()
    category = models.ManyToManyField(PostCategory)
    meta_description = models.CharField(max_length=10000)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Post")
        ordering = ("-timestamp",)

    def __str__(self):
        return self.post_title

    def snippet(self):
        return self.post_content[:105] + "..."

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)