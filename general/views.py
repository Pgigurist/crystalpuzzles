from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'general/index.html')

def about(req):
    return render(req, 'general/about.html')
