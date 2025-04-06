from django.db import models
from django.db.models import IntegerField


# Create your models here.

class MyQuiz(models.Model):
    name = models.CharField(max_length=256, help_text='Enter a quiz name')
    def __str__(self):
        return self.name

class QuizQuestion(models.Model):
    text_question = models.CharField(max_length=1024)
    image_question = models.ImageField()
    option1 = models.CharField(max_length=64)
    option2 = models.CharField(max_length=64)
    option3 = models.CharField(max_length=64)
    option4 = models.CharField(max_length=64)
    correct_option = IntegerField()
    quiz = models.ForeignKey('MyQuiz', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.text_question