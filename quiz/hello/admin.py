from django.contrib import admin

# Register your models here.
from .models import MyQuiz, QuizQuestion

admin.site.register(MyQuiz)
admin.site.register(QuizQuestion)