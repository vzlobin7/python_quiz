from django.shortcuts import render
from .models import QuizQuestion

def index(request):
#    return HttpResponse("Hello METANIT.COM")
    q = QuizQuestion.objects.first()
    return render(
        request,
        'index.html',
        context={'question':q.text_question,
                 'image':q.image_question,
                 'option1':q.option1,
                 'option2':q.option2,
                 'option3':q.option3,
                 'option4':q.option4},
    )