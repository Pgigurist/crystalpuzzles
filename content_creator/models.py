from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Athlet(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name=_('Имя')
            )
    family_name = models.CharField(max_length=100, verbose_name=_('Фамилия'))
    birth = models.DateField(verbose_name=_('Дата рождения'))
    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
    def __str__(self):
        return self.name+' '+self.family_name

class Element(models.Model):

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    ELEMENT_TYPE = (
        ('J', 'Прыжки'),
        ('M', 'Шаги'),
        ('S', 'Вращения')
    )
    name = models.CharField(
            max_length=30,
            verbose_name=_('название')
            )

    e_type = models.CharField(
            max_length=1,
            choices=ELEMENT_TYPE,
            verbose_name=_('тип')
    )
       
    def __str__(self):
        return self.name

class Lesson(models.Model):
    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    date = models.DateField(
            verbose_name = _('Дата занятия')
            )
    athlet = models.ForeignKey(
            Athlet,
            related_name='athlet_id',
            on_delete=models.CASCADE,
            verbose_name = _('ребенок')
            )
    def __str__(self):
        return self.athlet.name+' '+self.athlet.family_name+' '+str(self.date)

class ExecutedElement(models.Model):
    ELEMENT_MARK = (
        ('1', '1'), 
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    lesson = models.ForeignKey(
            Lesson,
            related_name = 'lesson_id',
            on_delete = models.CASCADE,
            verbose_name = _('занятие')
            )
    element = models.ForeignKey(
            Element,
            related_name = 'element_id',
            on_delete = models.CASCADE,
            verbose_name = _('элемент'),
            )
    mark = models.CharField(
            max_length = 1,
            choices = ELEMENT_MARK,
            blank = True,
            )
    repetitions = models.IntegerField(
            default=1,
            verbose_name=_('повторения')
    )

    def __str__(self):
        return self.element.name

