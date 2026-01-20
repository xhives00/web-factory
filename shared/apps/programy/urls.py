from django.urls import path
from . import views

urlpatterns = [
    path("", views.programy_index, name="programy_index"),
    path("<slug:program_slug>/", views.program_detail, name="program_detail"),
]

