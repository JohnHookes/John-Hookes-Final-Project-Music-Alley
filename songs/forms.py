from .models import Comment
from .models import Songs
from django import forms


class SongsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SongsPostForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ('title', 'slug', 'description', 'song_image', 'song_video_url', 'status', )

