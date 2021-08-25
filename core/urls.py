from django.urls import path, re_path
from .views import home, alumni, gallery

app_name = "core"

urlpatterns = [

    path('', home, name="home"),
    path('alumni', alumni, name="alumni"),
    path('gallery', gallery, name="gallery"),

]

# handler404 = handler404
# handler500 = handler500
