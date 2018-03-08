from django.shortcuts import render
from . import models


def index(request):
    """
    List some question
    """
    question_list = models.Question.objects.all()[:5]
    template_name = 'polls/index.html'
    return render(request, template_name, {
        'question_list': question_list,
    })
