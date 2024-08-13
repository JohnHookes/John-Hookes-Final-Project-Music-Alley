from django.db import models
from artists.models import Post
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Songs(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='default-slug',)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="song_posts", default=1)  
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    artist_name = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="song_posts", blank=True, null=True )
    song_image = CloudinaryField('image', default='placeholder')
    song_video_url = models.URLField(max_length=300, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now,)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"


    def get_embed_url(self):
        if 'youtube.com' in self.song_video_url or 'youtu.be' in self.song_video_url:
            # Handle YouTube URLs
            video_id = self.video_url.split('v=')[-1] if 'v=' in self.song_video_url else self.song_video_url.split('/')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.song_video_url  # If not YouTube, just return the URL (or handle other services similarly)

class Comment(models.Model):
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE, related_name="song_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="songs_commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} | written by {self.author}"

