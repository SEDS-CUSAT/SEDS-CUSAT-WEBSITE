from django.shortcuts import render
from .models import About, Project, Blog, Team, Alumni, Gallery

# from .models import HomeImage


# Create your views here.
def home(request):
    # length = len(HomeImage.objects.all())
    # events_length = len(Event.objects.all())
    # n1 = abs(events_length - 3)
    # n = abs(length - 3)
    #
    context = {
        'projects': Project.objects.all(),
        'blogs ': Blog.objects.all(),
        'gallery': Gallery.objects.all(),
    }
    return render(request, "home.html", context)

# Team function

def alumni(request):
    context = {
        'alumni': Alumni.objects.all(),
    }
    return render(request, "alumni_page.html", context)


def gallery(request):
    context = {
        'images': Gallery.objects.all()
    }
    return render(request, "gallery_page.html", context)

def teams(request):
    return render(request, "team_page.html")

# error handler
# def handler404(request, exception):
#     return render(request, '404.html', status=404)
#
#
# def handler500(request):
#     return render(request, '500.html', status=500)
