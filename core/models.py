from django.db import models
from django.utils import timezone

# Create your models here.
# class HomeImage(models.Model):
#
#     title = models.CharField(max_length=100, default="Home Image title")
#     sub_title = models.CharField(max_length=100, default="Home Image sub title")
#     description = models.CharField(max_length=300, default="description")
#     image = models.ImageField(default="image",upload_to="homeimage/")
#
#     def __str__(self):
#         return self.title
#
#
# class Event(models.Model):
#
#     CHOICES = (
#         ('N', 'No'),
#         ('Y', 'Yes')
#     )
#
#     title = models.CharField(max_length=100, default="Event title")
#     sub_title = models.CharField(max_length=100, default="Event sub title")
#     description = models.TextField(max_length=1200, default="description")
#     image = models.ImageField(default="image",upload_to="events/")
#     isopen = models.CharField(choices=CHOICES, max_length=100, default="No")
#     event_day = models.DateField(default=timezone.now())
#     registration_link = models.CharField(max_length=100, default="#")
#
#     def __str__(self):
#         return self.title
#
#
# class Project(models.Model):
#
#     title = models.CharField(max_length=100, default="Project Title")
#     sub_title = models.CharField(max_length=100, default="Project sub title")
#     description = models.CharField(max_length=300, default="description")
#     image = models.ImageField(default="image",upload_to="projects/")
#
#     def __str__(self):
#         return self.title
#
#
# class Gallery(models.Model):
#
#     title = models.CharField(max_length=100, default="Gallery image Title")
#     sub_title = models.CharField(max_length=100, default="Gallery image sub title")
#     image = models.ImageField(default="image", upload_to="gallery/")
#
#     def __str__(self):
#         return self.title
