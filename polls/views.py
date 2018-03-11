from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone

from . import models


class IndexView(generic.ListView):
    """
    List latest question
    """
    template_name = 'polls/index.html'
    model = models.Question

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(
            pub_date__lte=timezone.now()
        ).exclude(choice__isnull=True).order_by('-pub_date')[:5]


class QuestionDetail(generic.DetailView):
    model = models.Question
    template_name = 'polls/poll_detail.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(
            pub_date__lte=timezone.now()
        ).exclude(choice__isnull=True)


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
