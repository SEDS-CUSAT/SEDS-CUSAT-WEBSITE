from django.db import models


# Sharun's model
# About model
class About(models.Model):
    image = models.ImageField(default="image", upload_to="about/")


# Event model


# Project model
class Project(models.Model):
    title = models.CharField(max_length=100, default="Project Title")
    description = models.CharField(max_length=300, default="Project Description")
    image = models.ImageField(default="image", upload_to="project/")

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


# Alumni model
class Alumni(models.Model):
    name = models.CharField(max_length=100, default="name")
    designation = models.CharField(max_length=100, default="designation")
    image = models.ImageField(default="image", upload_to="alumni/")
    social = models.URLField(max_length=250)


# Gallery model
class Gallery(models.Model):
    image = models.ImageField(default="image", upload_to="gallery/")
