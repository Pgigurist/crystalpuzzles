from django.contrib import admin
from .models import Athlet, Element, Lesson, ExecutedElement

# Register your models here.

class ExecutedElementInline(admin.TabularInline):
    model = ExecutedElement

class LessonAdmin(admin.ModelAdmin):
    inlines = [
            ExecutedElementInline,
            ]

admin.site.register(Athlet)
admin.site.register(Element)
admin.site.register(Lesson, LessonAdmin)
