# gigs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_gigs, name='gigs'),
   
]