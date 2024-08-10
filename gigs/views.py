from django.shortcuts import render
from .models import Gigs
# Create your views here.


def about_gigs(request):
    """
    Renders the About page
    """
    gigs = Gigs.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "gigs/gigs.html",
        {"gigs": gigs},
    )