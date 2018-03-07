from django.db import models
from django.urls import reverse


class Question(models.Model):
    """
    Abstracts a particular question
    """
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date Published')

    class Meta:
        ordering = ['-pub_date', 'question_text', ]

    def get_absolute_url(self, *args, **kwargs):
        return reverse('polls:question-detail', args=[str(self.pk)])

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    Abstracts a Choice a particular question
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['question', '-votes', ]

    def __str__(self):
        return self.choice_text