from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, blogposts, images, comment

# Register your models here.

UserAdmin.fieldsets[1][1]["fields"] += ('user_quote',
                                        'user_bio', 'user_profile')

admin.site.register(User, UserAdmin)


class postAdminModel(admin.ModelAdmin):
    list_display = ("post_title", "post_date", "post_author")


class commentAdminModel(admin.ModelAdmin):
    list_display = ("comment_name", "comment_post",
                    "comment_date", "comment_moderated")
    list_filter = ('comment_date', "comment_moderated")


class imageAdminModel(admin.ModelAdmin):
    list_display = ("imagefile", "imagedate")


# registrando las bases de datos para mostrarlas en el admin site
admin.site.register(blogposts, postAdminModel)
admin.site.register(comment, commentAdminModel)
admin.site.register(images, imageAdminModel)
