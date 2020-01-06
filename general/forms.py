from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'city', 'text')

    """
    name = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.Textaria)
    text = forms.CharField(max_length=500, widget=forms.TextInput({}))
    """
