from django.shortcuts import render
from .models import Athlet, Lesson, ExecutedElement, Element
# Create your views here.

def getAthlets(req):
    content = {
            'athlets' : Athlet.objects.order_by('family_name', 'name')
    }
    return render(req, 'content_creator/athlet_list.html', content)

def getLessonsByAthlet(req, athlet):
    content = {
            'lessons' : Lesson.objects.filter(athlet_id=athlet)
    }
    return render(req, 'content_creator/lessons.html', content)

def detalis(req, lesson):
    content = {
            'elements' : ExecutedElement.objects.filter(lesson_id=lesson)
    }
    return render(req, 'content_creator/detalis.html', content)
