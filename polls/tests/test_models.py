import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):
    def test_published_recently_with_future_question(self):
        """
        published_recently() returns False for question with future
        pub_date
        """
        future_time = timezone.now() + datetime.timedelta(days=10)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_with_old_question(self):
        """
        published_recently() method returns False for question with
        pub_date older than 5 hours
        """
        old_time = timezone.now() - datetime.timedelta(hours=6)
        old_question = Question(pub_date=old_time)
        self.assertIs(old_question.published_recently(), False)

    def test_published_recently_with_recent_question(self):
        """
        published_test() method returns True for questions with
        pub_date within the last 5 hours
        """
        recent_time = timezone.now() - datetime.timedelta(hours=4, minutes=59)
        recent_question = Question(pub_date=recent_time)
        self.assertIs(recent_question.published_recently(), True)
