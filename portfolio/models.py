from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ProjectType(models.Model):
    project_type = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Project Type")
        verbose_name_plural = ("Project Type")
        ordering = ("-timestamp",)

    def __str__(self):
        return self.project_type


class Portfolio(models.Model):
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    client = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to="project/images")
    project_video = models.FileField(upload_to="project/videos", null=True, blank=True)
    preview_link = models.URLField()
    project_description = RichTextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Portfolio")
        verbose_name_plural = ("Portfolio")
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.client} Project"