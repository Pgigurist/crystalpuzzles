from django.contrib import admin
from .models import Athlet, Element, Lesson, ExecutedElement

# Register your models here.
class ExecutedElementAdmin(admin.ModelAdmin):
    """
    def  getNameFromLesson(self, instance):
        name = self.lesson.athlet
        return name
    """
    list_display = ('lesson', 'element', 'repetitions', 'mark')


class ExecutedElementInline(admin.TabularInline):
    model = ExecutedElement
    list_display = ('lesson', 'element', 'repetitions', 'mark')

class ElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'e_type')

class LessonAdmin(admin.ModelAdmin):
    inlines = [
            ExecutedElementInline,
            ]



admin.site.register(Athlet)
admin.site.register(Element)
#admin.site.register(ExecutedElement, ExecutedElementAdmin)
admin.site.register(Lesson, LessonAdmin)
