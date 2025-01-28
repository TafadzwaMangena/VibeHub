from django.shortcuts import render
from .models import About


def about_vibehub(request):
    """
    Renders the About page
    """
    about = About.objects.all().first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )