from django.contrib import admin
from .models import blogposts, images

# Register your models here.

#registrando las bases de datos para mostrarlas en el admin site
admin.site.register(blogposts)
admin.site.register(images)