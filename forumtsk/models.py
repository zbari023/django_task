from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager

# Create your models here, python manage.py makemigrations , python manage.py migrate

class Question(models.Model):
    question = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now , blank=True)
    tags = TaggableManager()
    def __str__(self):
        return self.question
    
class Answer(models.Model):
    question = models.ForeignKey(Question,related_name='Question_Answer',on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now , blank=True)
    answer = models.TextField(max_length=1000)
    def __str__(self):
        return self.answer
    
    