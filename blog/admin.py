from django.contrib import admin
from .models import PostCategory, Post

# Register your models here.

admin.site.register(PostCategory)

class PostAdmin(admin.ModelAdmin):
    fields = ["post_title", "post_image", "post_content", "meta_description", "category"]
    list_display = ("post_title", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("post_title", "post_content")
admin.site.register(Post, PostAdmin)