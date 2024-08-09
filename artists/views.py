from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "artists/post_detail.html",
        {"post": post, 
        "coder": "John Hookes"},
    )