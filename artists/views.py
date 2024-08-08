from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Post

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "artists/index.html"
    paginate_by = 6 