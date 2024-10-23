from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, ArtistPostForm
from django import forms
from django.contrib.auth.decorators import login_required

class HomePage(TemplateView):
    template_name = 'index.html'
    # artist_post_form = ArtistPostForm
    # form_class = ArtistPostForm
    # artist_post_form = ArtistPostForm()
    
    """
    Displays home page
    """

  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_post_form'] = ArtistPostForm()
        print("Form added to context in get_context_data:", context['artist_post_form'])
        return context

    def post(self, request, *args, **kwargs):
        artist_post_form = ArtistPostForm(data=request.POST)
        print("Received a POST request")
        if artist_post_form.is_valid():
            post = artist_post_form.save(commit=False)
            post.author = request.user
            post.save()
            print("Post saved successfully")
            return redirect('home')
        else:
            print("Form is not valid")

            # Re-render the template with the form context
        return render(request, "index.html", {
            "artists": artist,
            "artist_post_form": artist_post_form,
            "coder": "John Hookes",
            })



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_post_form'] = ArtistPostForm()
        return context

    def post(self, request, *args, **kwargs):
        artist_post_form = ArtistPostForm(request.POST, request.FILES)  # Handle file uploads
        if artist_post_form.is_valid():
            post = artist_post_form.save(commit=False)
            post.author = request.user
            post.save()
            print("Post saved successfully")
            messages.add_message(request, messages.SUCCESS, 'Artist Posting Saved!')
            return HttpResponseRedirect(reverse('home'))
        else:
            print("Form is not valid")
            messages.add_message(request, messages.ERROR, 'Error Creating Artist Posting! ')

            # Re-render the template with the form context
        return render(request, "index.html", {
            "artist_post_form": artist_post_form,
            "coder": "John Hookes",
            })

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
    post = get_object_or_404(queryset, slug=slug, status=1)
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

# function for editing a comment
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

# function for deleting a comment

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

def index(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'index.html', {
        'post': post,
        'comment_form': comment_form,
    })

# function for editing an artist Post

def post_edit(request, slug, post_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post = get_object_or_404(Post, pk=post_id)
        artist_post_form = ArtistPostForm(data=request.POST, instance=post)

        if artist_post_form.is_valid() and post.author == request.user:
            post = artist_post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Artist Post Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Artist Post!')

    return HttpResponseRedirect(reverse('home', args=[slug]))

# function for deleting an Artist Post
def post_delete(request, slug, post_id):
    """
    view to delete post
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
  #  comment = get_object_or_404(Comment, pk=comment_id)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own post!')

    return HttpResponseRedirect(reverse('home',))

def index(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        artist_post_form = ArtistPostForm(request.POST)
        if artist_post_form.is_valid():
            post = post_form.save(commit=False)
            post.post = post
            post.author = request.user
            post.save()
    else:
        artist_post_form = ArtistPostForm()

    return render(request, 'index.html', {
        'post': post,
        'artist_post_form': artist_post_form,
    })

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
        return redirect('home')  # Redirect to an appropriate page after deletion
    else:
        return redirect('post_detail', post_id=post_id)  # If the user is not authorized
