from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blogentry/<int:id>/', views.blogEntry, name='blogentry'),
    path('accounts/login/', views.logginview, name='loggin'),
    path('logout', views.logoutview, name='logout'),


    path('administration/resources',
         views.administration_resources, name="admin_resources"),
    path('resource/<int:id>/remove',
         views.administration_delete_resource, name='admin_delete_resource'),


    path('administracion', views.administration_entries, name='admin_entries'),
    path('administration/create', views.administration_create_entry,
         name="admin_create_entry"),
    path('post/<int:id>/delete',
         views.administration_delete_entry, name='admin_delete_entry'),
    path('post/<int:id>/update',
         views.administration_update_entry, name='admin_update_entry'),


    path('admnistration/comments',
         views.administration_comments, name='admin_comments'),
    path('comment/<int:id>/delete',
         views.administration_delete_comment, name='admin_delete_comment'),
    path('comment/<int:id>/update',
         views.administration_update_comment, name='admin_update_comment'),

]
