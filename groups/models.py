from django.db import models

# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=300)
    #image = models.ImageField(upload_to='media/images/')
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title


