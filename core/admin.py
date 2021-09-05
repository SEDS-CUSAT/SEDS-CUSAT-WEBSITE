from django.contrib import admin
from .models import About, Project, Blog, Team, Alumni, Gallery

# Register your models here.
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Alumni)
admin.site.register(Gallery)
admin.site.site_header = "Admin"
admin.site.site_title = " Admin Portal"
admin.site.index_title = "Welcome to SEDS CUSAT Admin Portal"
