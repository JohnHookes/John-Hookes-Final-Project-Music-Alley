# songs/urls.py
from . import views
from django.urls import path
from .views import songs_detail

urlpatterns = [
    path("", views.songs_detail, name='songs'),
    path('<slug:slug>/', views.songs_detail, name='songs_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]