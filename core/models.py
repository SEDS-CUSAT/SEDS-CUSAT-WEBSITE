from django.db import models
from django.utils import timezone


# Sharun's model
# About model
class About(models.Model):
    image = models.ImageField(default="image", upload_to="about/")
    description = models.CharField(max_length=3000, default="About Description")
def __str__(self):
        return self.title
# Event model


# Project model
class Project(models.Model):
    title = models.CharField(max_length=100, default="Project Title")
    description = models.CharField(max_length=300, default="Project Description")
    image = models.ImageField(default="image", upload_to="project/")
    link = models.CharField(max_length=100,default="#")

    def __str__(self):
        return self.title


# Blogs model
class Blog(models.Model):
    title = models.CharField(max_length=100, default="Blog Title")
    author = models.CharField(max_length=20, default='Blog Author')
    description = models.CharField(max_length=300, default="description")
    published = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(default="image", upload_to="blog/")

    def __str__(self):
        return self.title

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, default="name")
    designation = models.CharField(max_length=100, default="designation")
    image = models.ImageField(default="image", upload_to="team/")

    def __str__(self):
        return self.title


# Alumni model
class Alumni(models.Model):
    name = models.CharField(max_length=100, default="name")
    designation = models.CharField(max_length=100, default="designation")
    description = models.CharField(max_length=1200, default="description")
    image = models.ImageField(default="image", upload_to="alumni/")
    social = models.URLField(max_length=250)


    def __str__(self):
        return self.title

# Gallery model
class Gallery(models.Model):
    image = models.ImageField(default="image", upload_to="gallery/")

    def __str__(self):
        return self.title
#event model
class Event(models.Model):

    title = models.CharField(max_length=100, default="Event title")
    location = models.CharField(max_length=100, default="Event location")
    description = models.TextField(max_length=1200, default="description")
    image = models.ImageField(default="image",upload_to="events/")
    event_day = models.DateField(default=timezone.now())
    event_time = models.TimeField(default=timezone.now())
    registration_link = models.CharField(max_length=100, default="#")
def __str__(self):
    return self.title

class SocialMedia(models.Model):

    insta_link = models.CharField(max_length=100, default="#")
    fb_link = models.CharField(max_length=100, default="#")
    twitter_link = models.CharField(max_length=100, default="#")
    linkedin_link = models.CharField(max_length=100, default="#")
    medium_link = models.CharField(max_length=100, default="#")
def __str__(self):
        return self.title

