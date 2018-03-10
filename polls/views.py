from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


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
        'form': forms.PollForm,
    })


def result(request, pk):
    """
    Display a particular question voting results
    """
    question = get_object_or_404(models.Question, pk=pk)
    template_name = 'polls/poll_result.html'
    return render(request, template_name, context={
        'question': question,
    })


def vote(request, pk):
    """
    Takecare voting of a particular poll
    """
    if request.method == 'POST':
        question = get_object_or_404(models.Question, pk=pk)

        try:
            selected_choice = question.choice_set.get(
                pk=request.POST['choice']
            )
        except:
            return render(
                request,
                'polls/poll_detail.html',
                context={
                    'error_message': 'You did not select any choice',
                    'question': question,
                }
            )
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:poll-result', pk=pk)
    return render(request, 'polls/poll_detail.html')
