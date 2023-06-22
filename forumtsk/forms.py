from django import forms
from .models import Question

class Forumform(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'