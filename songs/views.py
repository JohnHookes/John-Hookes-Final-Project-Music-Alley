from django.shortcuts import render
from .models import Songs
# Create your views here.


def about_songs(request):
    """
    Renders the About page
    """
    songs = Songs.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "songs/songs.html",
        {"songs": songs},
    )