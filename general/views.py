from django.shortcuts import render
from .models import Post, Photo, Feedback
from .forms import FeedbackForm
### import sberbank
from sberbank.service import BankService
from sberbank.models import Payment, Status

# Create your views here.

def index(req):
    context = {
            'photos': Photo.objects.all()[:3],
            'posts' : Post.objects.all().order_by('pub_date').reverse()[:3]
            }
    return render(req, 'general/index.html', context)

def about(req):
    return render(req, 'general/about.html')

def news(req):
    context = {'posts' : Post.objects.all().order_by('pub_date').reverse()}
    return render(req, 'general/news.html', context)

def gallery(req):
    context = {'photos' : Photo.objects.all().reverse()}
    return render(req, 'general/gallery.html', context)

def addFeedback(req):
    """
        добавляет левый отзыв/ fixed
    """
    posts = Feedback.objects.all().order_by('pub_date').reverse()
    
    if req.method == 'POST':
        form = FeedbackForm(req.POST)
        if form.is_valid():
            feedback = form.save()
            print(feedback)
            feedback.save()
            return render(req, 'general/index.html')
    else:
        form = FeedbackForm()
        context = {
            'posts'  :   posts,
            'feedback_form' : form,
        }
    return render(req,  'general/feedback.html', context)

def payment(req):
    print('payment request')
    pass

