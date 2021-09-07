from django.urls import path
from .views import home, alumni, gallery, teams

app_name = "core"

urlpatterns = [

    path('', home, name="home"),
    path('alumni', alumni, name="alumni"),
    path('gallery', gallery, name="gallery"),
    path('teams', teams, name="teams"),

]

# handler404 = handler404
# handler500 = handler500
