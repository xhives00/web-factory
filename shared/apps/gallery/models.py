from django.db import models

class GalleryEvent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-date", "title"]

    def __str__(self) -> str:
        return self.title

class GalleryImage(models.Model):
    event = models.ForeignKey(GalleryEvent, on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title or f"Image #{self.pk}"
