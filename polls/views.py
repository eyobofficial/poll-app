from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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


def detail(request, pk):
    """
    Display a particular question and voting form without the results
    """
    question = get_object_or_404(models.Question, pk=pk)

    template_name = 'polls/poll_detail.html'
    return render(request, template_name, context={
        'question': question,
    })


def result(request, pk):
    """
    Display a particular question voting results
    """
    template_name = 'polls/poll_result.html'
    return render(request, template_name, context={
        'pk': pk,
    })


def vote(request, pk):
    """
    Takecare voting of a particular poll
    """
    return HttpResponse('Vote for question no. {}'.format(pk))
