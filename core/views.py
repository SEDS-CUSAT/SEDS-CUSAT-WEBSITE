from django.shortcuts import render


# from .models import HomeImage


# Create your views here.
def home(request):
    # length = len(HomeImage.objects.all())
    # events_length = len(Event.objects.all())
    # n1 = abs(events_length - 3)
    # n = abs(length - 3)
    #
    # context = {
    #     "homeimage": HomeImage.objects.all()[n:],
    #     "events": Event.objects.all()[n1:]
    # }

    return render(request, "home.html")


def alumni(request):
    return render(request, "alumni_page.html")


def gallery(request):
    return render(request, "gallery_page.html")

# error handler
# def handler404(request, exception):
#     return render(request, '404.html', status=404)
#
#
# def handler500(request):
#     return render(request, '500.html', status=500)
