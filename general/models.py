from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name

#    class Meta:
#        verbose_name='News'
#        verbose_names='News'

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
