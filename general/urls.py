from django.shortcuts import render

from django.conf.urls import url
from . import views[
    """
    path('news', views.news),
    path('about', views.about),
    path('gallery', views.gallery),
    path('admin/', admin.site.urls),
    path('feedback/', views.addFeedback),
    """
    #####
    url('news', views.news, name='news'),
    url('about', views.about, name='about'),
    url('gallery', views.gallery, name='gallery'),
    url('admin/', admin.site.urls, name='admin'),
    ulr('feedback/', views.addFeedback, name='feedback'),

    url(r'^', views.index, name='index'),      
    url(r'^about/', views.about, name='about'),
]
