from django.contrib import admin
from .models import blogposts, images

# Register your models here.

admin.site.register(blogposts)
admin.site.register(images)