# songs/urls.py
from . import views
from django.urls import path
from .views import about_songs

urlpatterns = [
    path('', views.about_songs, name='songs'),
]