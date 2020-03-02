from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

""" Find out how to filter through by day month and year """
""" Desplay events cronologicalls by date of the event """

class Event(models.Model):

    name = models.CharField(max_length=100, blank=False, default='', null=True)
    coordinator = models.ForeignKey(User, blank=True, null=True, default='',on_delete=models.PROTECT, help_text="The user that posted this article.")
    slug = models.CharField(max_length=settings.WIKI_PAGE_TITLE_MAX_LENGTH, blank=True, editable=False, help_text="Unique URL path to access this page. Generated by the system.")
    details = models.TextField(help_text="Write the details of your page here.", null=True, default='')
    created = models.DateTimeField(auto_now_add=True, help_text="The date and time this page was created. Automatically generated when the model saves.")
    event_date = models.DateField(blank=False, null=False)
    event_time = models.TimeField(auto_now=False, auto_now_add=False)
    modified = models.DateTimeField(auto_now=True, help_text="The date and time this page was updated. Automatically generated when the model updates.")
    contact_person = models.CharField(max_length=100, blank=False, default='', null=False)
    #type_of_event(dropdown menu of options, brunch, dinner, cocktails, ect...)
    #number_of_guests
    location = models.CharField(max_length=100, blank=False, default='', null=False)
    #deposite confirmed


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'slug': self.slug}
        return reverse('event-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(Event, self).save(*args, **kwargs)
