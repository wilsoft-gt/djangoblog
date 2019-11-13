from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blog', views.blog, name='blog'),
    path('blogentry', views.blogEntry, name='blogentry'),
    path('newpost', views.createEntry, name='newpost'),
    path('resources', views.resources, name='resources'),
    path('accounts/login/', views.logginview, name='loggin'),
    path('logout', views.logoutview, name='logout'),
    path('remove', views.removeresource, name='removeresource'),
    path('administracion', views.administration, name='administration'),
]
