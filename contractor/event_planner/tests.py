import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Events

# Create your tests here.

class EventModelTests(TestCase):
    def test_was_published_recently_with_future_event(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(pub_date=time)
        self.assertIs(future_event.was_published_recently(), False)

    def test_was_published_recently_with_old_event(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_event = Question(pub_date=time)
        self.assertIs(old_event.was_published_recently(), False)

    def test_was_published_recently_with_recent_event(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_event = Event(pub_date=time)
        self.assertIs(recent_event.was_published_recently(), True)

def create_event(event_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Event.objects.create(event_text=event_text, pub_date=time)
