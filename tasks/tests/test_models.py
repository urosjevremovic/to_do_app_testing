from unittest import TestCase

from tasks.models import Task

from django.utils import timezone


class ClassModelTestCase(TestCase):

    def test_complete_model_is_complete(self):
        target = Task()
        target.complete_time = timezone.now() - timezone.timedelta(days=1)

        self.assertTrue(target.is_complete)

    def test_incomplete_model_is_incomplete(self):
        target = Task()
        target.complete_time = None

        self.assertFalse(target.is_complete)

    def test_future_complete_model_is_incomplete(self):
        target = Task()
        target.complete_time = timezone.now() + timezone.timedelta(days=1)

        self.assertFalse(target.is_complete)
