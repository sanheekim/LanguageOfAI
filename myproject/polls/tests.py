from django.test import TestCase

# Create your tests here.

# 버그 노출하는 테스트 만들기 2022.08.08.(월)
# 아래 코드 작성 후 터미널에 테스트 실행 : py manage.py test polls
# test 통과 안 될 예정.
# 그럼 polls/models.py로 이동해서 통과할 수 있는 코드 작성.
import datetime
from django.utils import timezone
from .models import Question
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)