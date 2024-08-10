from django.shortcuts import render
from .models import Albums
# Create your views here.


def albums(request):
    """
    Renders the About page
    """
    albums = Albums.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "albums/albums.html",
        {"albums": albums},
    )