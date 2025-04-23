from django.shortcuts import render
from .models import QuizQuestion, MyQuiz

from django.views import generic

class QuizListView(generic.ListView):
    model = MyQuiz

def question(request, id):
    q = QuizQuestion.objects.get(id=id)
    return render(
        request,
        'question.html',
        context={'question':q.text_question,'image':q.image_question,
                 'option1':q.option1,'option2':q.option2,'option3':q.option3,'option4':q.option4,
                 'correct_option':q.correct_option, 'question_count': QuizQuestion.objects.all().count()},
    )

