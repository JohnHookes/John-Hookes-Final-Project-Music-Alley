from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, ArtistPostForm
from django import forms

class HomePage(TemplateView):
    """
    Displays home page
    """

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_post_form'] = ArtistPostForm()
        return context

    def post(self, request, *args, **kwargs):
        artist_post_form = ArtistPostForm(data=request.POST)
        print("Received a POST request")
        if artist_post_form.is_valid():
            post = artist_post_form.save(commit=False)
            post.author = request.user  # Assuming 'author' is a field on your Post model
            post.save()
            print("Post saved successfully")
        else:
            print("Form is not valid")

        # Re-render the template with the form context
        return render(request, self.template_name, {
            "artist_post_form": artist_post_form,
            "coder": "John Hookes",
        })

"""


    """
    template_name = 'index.html'
    artist_post_form = ArtistPostForm()
    
    if request.method == "POST":
        artist_post_form = ArtistPostForm(data=request.POST)
        print("Received a POST request")
        if artist_post_form.is_valid():
            post = artist_post_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    artist_post_form = ArtistPostForm()
    print("About to render template")

    return render(request, "artists/index.html",
        {"post": post, 
        "coder": "John Hookes",
        "artist_post_form": artist_post_form, },
    )

    """

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "artists/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`artists.Post`.

    **Context**

    ``post``
        An instance of :model:`artists.Post`.

    **Template:**

    :template:`artists/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        print("Received a POST request")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    comment_form = CommentForm()
    print("About to render template")

    return render(request, "artists/post_detail.html",
        {"post": post, 
        "coder": "John Hookes",
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form, },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
