from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.CharField(max_length=150)

# Create your models here.
