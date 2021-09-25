from django.db import models
from django.utils.timezone import now


# About model
class About(models.Model):
    title = models.CharField(max_length=100, default="Image Title")
    image = models.ImageField(default="image", upload_to="about/")
    description = models.CharField(max_length=3000, default="About Description")

    def __str__(self):
        return self.title


# Event model
class Event(models.Model):
    title = models.CharField(max_length=100, default="Event title")
    location = models.CharField(max_length=100, default="Event location")
    location_url = models.CharField(max_length=100, default="#")
    description = models.TextField(max_length=1200, default="description")
    image = models.ImageField(default="image", upload_to="events/")
    event_day = models.DateField(default=now())
    event_time_start = models.TimeField(default=now())
    event_time_end = models.TimeField(default=now())
    registration_link = models.CharField(max_length=100, default="#")

    def __str__(self):
        return self.title


# Project model
class Project(models.Model):
    title = models.CharField(max_length=100, default="Project Title")
    description = models.CharField(max_length=300, default="Project Description")
    image = models.ImageField(default="image", upload_to="project/")
    link = models.CharField(max_length=100, default="#")

    def __str__(self):
        return self.title


# Blogs model
class Blog(models.Model):
    title = models.CharField(max_length=100, default="Blog Title")
    author = models.CharField(max_length=20, default='Blog Author')
    description = models.CharField(max_length=300, default="description")
    published = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(default="image", upload_to="blog/")
    medium_link = models.CharField(max_length=100, default="#")

    def __str__(self):
        return self.title


# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, default="name")
    designation = models.CharField(max_length=100, default="designation")
    image = models.ImageField(default="image", upload_to="team/")

    def __str__(self):
        return self.name


# Alumni category
class AlumniCategory(models.Model):
    categories = models.CharField(max_length=12, default='2021-2022')

    def __str__(self):
        return self.categories


# Alumni model
class Alumni(models.Model):
    duration = models.ForeignKey(AlumniCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, default="name")
    designation = models.CharField(max_length=100, default="designation")
    image = models.ImageField(default="image", upload_to="alumni/")
    social = models.URLField(max_length=250)

    def __str__(self):
        return self.name


# Gallery model
class Gallery(models.Model):
    title = models.CharField(max_length=100, default="Image Title")
    image = models.ImageField(default="image", upload_to="gallery/")

    def __str__(self):
        return self.title
