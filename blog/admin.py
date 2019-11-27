from django.contrib import admin
from .models import blogposts, images, comment, adminExtraField

# Register your models here.
class postAdminModel(admin.ModelAdmin):
    list_display = ("post_title", "post_date", "post_author")

class commentAdminModel(admin.ModelAdmin):
    list_display = ("comment_name", "comment_post", "comment_date", "comment_moderated")
    list_filter = ('comment_date', "comment_moderated")

class adminExtrafieldModel(admin.ModelAdmin):
    list_display = ("adminFields_user", "adminFields_bio")

class imageAdminModel(admin.ModelAdmin):
    list_display = ("imagefile", "imageuser", "imagedate")
#registrando las bases de datos para mostrarlas en el admin site
admin.site.register(blogposts, postAdminModel)
admin.site.register(comment, commentAdminModel)
admin.site.register(images, imageAdminModel)
admin.site.register(adminExtraField, adminExtrafieldModel)