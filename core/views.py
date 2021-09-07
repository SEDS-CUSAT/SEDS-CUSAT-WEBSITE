from django.shortcuts import render
from .models import About, Event, Project, Blog, Team, Alumni, Gallery


def home(request):
    context = {
        'about': About.objects.all()[0],
        'events': Event.objects.all(),
        'projects': Project.objects.all(),
        'blogs': Blog.objects.all(),
        'team': Team.objects.all(),
        'alumni': Alumni.objects.all(),
        'gallery': Gallery.objects.all(),
    }
    return render(request, "home.html", context)


def alumni(request):
    context = {
        'alumni': Alumni.objects.all(),
    }
    return render(request, "alumni_page.html", context)


def gallery(request):
    context = {
        'gallery': Gallery.objects.all()
    }
    return render(request, "gallery_page.html", context)


def teams(request):
    context = {
        'team': Team.objects.all(),
    }
    return render(request, "team_page.html", context)


# error handler
def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
