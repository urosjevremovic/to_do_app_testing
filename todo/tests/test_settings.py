from unittest import TestCase

from django.conf import settings


class SettingsTestCase(TestCase):

    def test_server_timezone_unchagned(self):

        target_timezone = 'UTC'
        self.assertEqual(target_timezone, settings.TIME_ZONE)