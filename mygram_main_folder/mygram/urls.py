"""Mygram URLs module"""
from django.urls import path
from django.contrib import admin
from mygram import views as local_views
from posts import views as posts_views

urlpatterns = [

    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),   
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),

    path('admin/', admin.site.urls),

]
