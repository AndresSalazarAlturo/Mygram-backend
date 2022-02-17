"""Mygram URLs module"""
from argparse import Namespace
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),

    #path('hello-world/', local_views.hello_world, name='hello_world'),  ##Con los nombres puedo cambiar las url
    #path('sorted/', local_views.sort_integers, name='sort'),            ##y django reconoce los path
    #path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    ##Le suma al urlpaterns una url statica con el valor de media url que tenemos y donde estamos
    ##parados en la media
