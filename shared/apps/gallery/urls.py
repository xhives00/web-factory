from django.urls import path
from . import views

urlpatterns = [
    path("", views.events, name="gallery_events"),
    path("<slug:slug>/", views.event_detail, name="gallery_event_detail"),
]
