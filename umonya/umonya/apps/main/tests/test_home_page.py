import datetime
import calendar
from django.utils import timezone
from django.test import TestCase
from umonya.apps.main import models


class TestIsValidDate(TestCase):
    """ Tests Announcement.is_valid_date by testing dates with known
    results or outputs"""

    def test_is_valid_date_tomorrow(self):
        pub_date = timezone.now().date()
        year = pub_date.year
        month = pub_date.month
        day = pub_date.day + 1
        if day < 1:
            day = calendar.monthrange(year, month - 1)[1]
        elif day > calendar.monthrange(year, month)[1]:
            day = 1
        event_date = datetime.date(year, month, day)
        test = models.Announcement(pub_date, event_date)
        self.assertEqual(True, test.is_valid_date())

    def test_is_valid_date_yesterday(self):
        pub_date = timezone.now().date()
        year = pub_date.year
        month = pub_date.month
        day = pub_date.day - 1
        if day < 1:
            day = calendar.monthrange(year, month - 1)[1]
        elif day > calendar.monthrange(year, month)[1]:
            day = 1
        event_date = datetime.date(year, month, day)
        test = models.Announcement(pub_date, event_date)
        self.assertEqual(False, test.is_valid_date())
