from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from event_planner.models import Event

from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
class EventListView(ListView):
    """ Renders a list of all Events. """
    model = Event

    def get(self, request):
        """ GET a list of Events. """
        events = self.get_queryset().all()
        return render(request, 'event-list.html',{
        'events': events
        })
