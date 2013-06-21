from django.core import mail
from django.test import TestCase
from django.core.mail import send_mail


class TestEmail(TestCase):
    def test_send_email(self):
        send_mail("Subject", "Messsage", "fromgitumarkk@gmail.com", ["gitumarkk@gmail.com"],
                  fail_silently=False)

        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, "Subject")
