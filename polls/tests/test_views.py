import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


def create_question(question_text, days):
    """
    Create a new question and return it.
    +ve days are future days.
    -ve days are past days.
    """
    return Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() + datetime.timedelta(days=days)
    )


def create_choice(question, choice_text, votes=0):
    """
    Create a choice for a particular question
    """
    return question.choice_set.create(
        choice_text=choice_text,
        votes=votes
    )


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        No questions are published
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_question(self):
        """
        Question (with choices) with past pub_date is published
        """
        question = create_question(question_text='Past Question', days=-10)
        create_choice(question, 'Choice 1')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['question_list'],
            ['<Question: Past Question>']
        )

    def test_future_question(self):
        """
        Question (with choices) with future pub_date is published
        """
        question = create_question(question_text='Future Question', days=10)
        create_choice(question, 'Choice 1')
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(
            response.context['question_list'],
            []
        )

    def test_now_question(self):
        """
        Question (with choices) pub_date equals to now (Just Published)
        """
        question = create_question(question_text='Now Question', days=0)
        create_choice(question, 'Choice 1')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['question_list'],
            ['<Question: Now Question>']
        )

    def test_question_with_no_choices(self):
        """
        Past Questions with no choices
        """
        create_question('Question With No Choices', days=-10)
        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertQuerysetEqual(response.context['question_list'], [])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        Question (with choices) with pub_date in the future should not
        be displayed
        """
        future_question = create_question('Future Question', 10)
        create_choice(future_question, 'Choice 1')
        response = self.client.get(reverse(
            'polls:poll-detail',
            args=[future_question.id]
        ))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        Question (with choices) with pub_date in the past
        """
        past_question = create_question('Past Question', -10)
        create_choice(past_question, 'Choice 1')
        url = reverse('polls:poll-detail', args=[past_question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_question_with_no_choices(self):
        """
        Past Question with no choices
        """
        question = create_question('Question With No Choices', days=-10)
        url = reverse('polls:poll-detail', args=[question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_question_with_choices(self):
        """
        Past Question with choices
        """
        question = create_question('Question With Choices', days=-10)
        create_choice(question, 'Choice 1')
        url = reverse('polls:poll-detail', args=[question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)