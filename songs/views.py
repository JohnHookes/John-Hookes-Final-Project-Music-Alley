from django.shortcuts import render
from django.contrib import messages
from .models import Songs

# Create your views here.


def about_songs(request):
    
    
    """
    Renders the songs page
    """
    songs = Songs.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "songs/songs.html",
        {"songs": songs, },
    )
