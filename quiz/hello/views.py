from django.shortcuts import render
from .models import QuizQuestion, MyQuiz
import logging

from django.views import generic
logger = logging.getLogger(__name__)

class QuizListView(generic.ListView):
    model = MyQuiz

def question(request, quizid, id):
    #quiz = MyQuiz.objects.get(id=quizid)
    #logger.debug(QuizQuestion.objects.filter(quiz__id=quizid))
    a_count = QuizQuestion.objects.filter(quiz__id=quizid).count()
    #logger.debug(a_count)
    q = QuizQuestion.objects.filter(quiz__id=quizid)[id-1]
    return render(
        request,
        'question.html',
        context={'question':q.text_question,'image':q.image_question,
                 'option1':q.option1,'option2':q.option2,'option3':q.option3,'option4':q.option4,
                 'correct_option':q.correct_option, 'question_count': a_count},
    )

