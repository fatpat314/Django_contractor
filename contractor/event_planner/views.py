from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from event_planner.models import Event
from event_planner.forms import PageForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
        event = self.get_queryset().get(slug__iexact=slug)#Figure out how to name thow events the same name
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

@method_decorator([login_required], name='dispatch')
class EventEditView(UpdateView):
    model = Event
    fields = ['name', 'details', 'event_date', 'event_time', 'location']

    template_name = 'event_edit.html'
    success_url = reverse_lazy('event-list')


@method_decorator([login_required], name='dispatch')
class EventDeleteView(DeleteView):

    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('event-list')

class SearchResultsView(ListView):
    model = Event
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Event.objects.filter(

            Q(slug__icontains=query) | Q(event_date__icontains=query)
        )
        return object_list
