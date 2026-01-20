from django.urls import path
from .views import programy_home

urlpatterns = [
    path("", programy_home, name="programy_home"),
]
