from django.test import TestCase
from django.utils import timezone

from .models import Question

import datetime


class QuestionModelTests(TestCase):
    def test_published_recently_with_future_question(self):
        """
        published_recently() returns False for question with future
        pub_date
        """
        future_time = timezone.now() + datetime.timedelta(days=10)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.published_recently(), False)
