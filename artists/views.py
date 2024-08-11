from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    comment_form = CommentForm()

    return render(
        request,
        "artists/post_detail.html",
        {"post": post, 
        "coder": "John Hookes",
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form, },
    )