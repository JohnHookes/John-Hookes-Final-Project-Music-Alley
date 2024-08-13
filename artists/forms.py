from .models import Comment
from .models import Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ArtistPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('artist_name', 'title', 'slug', 'about', 'featured_image', 'genre', 'video_url', 'status', 'excerpt',)

