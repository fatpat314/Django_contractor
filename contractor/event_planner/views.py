from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from event_planner.models import Event
from event_planner.forms import PageForm

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

class EventDetailView(DetailView):
    """render a specific event based on its slug"""
    model = Event

    def get(self, request, slug):
        '''Return a specific event page by slug'''
        event = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html',{
            'event': event
        })

class New_event_form(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form':PageForm()}
        return render(request, 'new-event-form.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            new_event_form = form.save()
            return HttpResponseRedirect(reverse_lazy('event-details-page', args=[new_event_form.slug]))
        return render(request, 'new-event-form.html', {'form':form})
