from django.shortcuts import render

from . import views[
    url(r'^', views.index, name='index'),        
    url(r'^about/', views.about, name='about')
]
