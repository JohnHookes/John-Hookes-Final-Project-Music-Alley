from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

#Artist posting Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
#need to connect to artist class? not user    
    author = models.ForeignKey(
       User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    artist_name = models.CharField(max_length=50, blank=True)
    about = models.TextField(blank=True)
    genre = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    video_url = models.URLField(max_length=300, blank=True, null=True)
    #image = models.ImageField(upload_to=artists_images/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"


    def get_embed_url(self):
        if 'youtube.com' in self.video_url or 'youtu.be' in self.video_url:
            # Handle YouTube URLs
            video_id = self.video_url.split('v=')[-1] if 'v=' in self.video_url else self.video_url.split('/')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.video_url  # If not YouTube, just return the URL (or handle other services similarly)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} | written by {self.author}"





