from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    created_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self) -> str:
        return self.title
