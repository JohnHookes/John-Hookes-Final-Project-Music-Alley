from .models import Comment
from .models import Gigs
from django import forms


class GigsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class GigsPostForm(forms.ModelForm):
    class Meta:
        model = Gigs
        fields = ('artist_name', 'city', 'title', 
        'description', 'gig_image', 'venue', 'date_of_gig', 
        'time_of_gig', 'price', 'gig_image', 'status',)

