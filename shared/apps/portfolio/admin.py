from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "link")
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
