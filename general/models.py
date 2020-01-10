from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.title


class Post(models.Model):
    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self):
        return self.name

#    class Meta:
#        verbose_name='News'
#        verbose_names='News'

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    moderate = models.BooleanField(default=False)

    def __str__(self):
        string = self.name
        if self.moderate:
            string += ' (опубликовано)'
        else:
            string += ' (новое)'
        return string
"""
    class Meta:
        verbose_name='Отзыв'
        verbose_names='Отзывы'
"""

