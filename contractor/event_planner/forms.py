from django import forms
from event_planner.models import Event


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta():
        model = Event
        fields = ['name', 'contact_person', 'coordinator', 'details', 'event_date', 'event_time', 'location']
