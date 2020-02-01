from django.conf.urls import url
from content_creator import views

urlpatterns = [  # noqa: pylint=invalid-name
        url(r'^ajax/$', views.ajax),
        url(r'^athlet_list/$', views.getAthlets),
        url(r'^athlet_list/(?P<athlet>[0-9])/$', views.getLessonsByAthlet, name = 'lessons'), 
        url(r'^athlet_list/detalis/(?P<lesson>[0-9])/$', views.detalis, name = 'detalis'), 
  ]
