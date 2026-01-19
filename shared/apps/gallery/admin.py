from django.contrib import admin
from .models import GalleryEvent, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(GalleryEvent)
class GalleryEventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GalleryImageInline]
