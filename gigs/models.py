from django.db import models
from artists.models import Post
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
class Gigs(models.Model):
    artist_name = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="gigs_posts", blank=True, null=True )
    slug = models.SlugField(max_length=200, unique=True, default='default-slug',) 
    city = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, blank=True, null=True)  # Optional description
    venue = models.CharField(max_length=200, blank=True)
    date_of_gig = models.DateField(default=timezone.now,)  # The date of the gig
    time_of_gig = models.TimeField(default=timezone.now,)  # The time of the gig
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    gig_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gigs_posts", blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(default=timezone.now,)

    def __str__(self):
        return f"{self.artist_name} will be playing at {self.time_of_gig} on {self.date_of_gig} at {self.venue} in {self.city}.  Tickets are £{self.city}"

class Comment(models.Model):
    gigs = models.ForeignKey(Gigs, on_delete=models.CASCADE, related_name="gigs_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gigs_commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} | written by {self.author}"
    




