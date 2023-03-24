from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blogentry/<int:id>/', views.blogEntry, name='blogentry'),
    path('newpost', views.createEntry, name='newpost'),
    path('resources', views.resources, name='resources'),
    path('accounts/login/', views.logginview, name='loggin'),
    path('logout', views.logoutview, name='logout'),
    path('resource/<int:id>/remove', views.removeresource, name='removeresource'),
    path('administracion', views.administration_entries, name='administration'),
    path('admnistration/comments',
         views.administration_comments, name='admin_comments'),
    path('administration/create', views.administration_create_entry,
         name="admin_create_entry"),
    path('administration/resources',
         views.administration_resources, name="admin_resources"),
    path('post/<int:id>/delete', views.postDelete, name='postDelete'),
    path('post/<int:id>/update', views.updatePost, name='postUpdate'),
    path('comments', views.commentsView, name='comments'),
]
