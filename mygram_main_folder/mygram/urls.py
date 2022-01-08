"""Mygram URLs module"""
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mygram import views as local_views
from posts import views as posts_views

urlpatterns = [

    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),   
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),

    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ##Le suma al urlpaterns una url statica con el valor de media url que tenemos y donde estamos
    ##parados en la media
