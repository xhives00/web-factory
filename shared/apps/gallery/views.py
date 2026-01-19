from django.shortcuts import get_object_or_404, render
from .models import GalleryEvent

def events(request):
    return render(request, "gallery/events.html", {"events": GalleryEvent.objects.all()})

def event_detail(request, slug: str):
    event = get_object_or_404(GalleryEvent, slug=slug)
    return render(request, "gallery/event_detail.html", {"event": event})
