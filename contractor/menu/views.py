from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View

from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from menu.models import MenuItem
from menu.forms import PageForm


# Create your views here.
class MenuListView(ListView):
    """Render List of Menu Items"""
    model = MenuItem

    def get(self, request):
        """Get a list of menu Items"""
        items = self.get_queryset().all()
        return render(request, 'menu/menu-list.html', {
        'items':items
        })

class MenuDetailView(DetailView):
    """ render a specific menu item based on its slug"""
    model = MenuItem

    def get (self, request, id):
        item = self.get_queryset().get(id=id)
        return render(request, 'menu/menu-detail-page.html',{
        'item':item
        })

class MenuCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form':PageForm()}
        return render(request, 'menu/new-menu-form.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse_lazy('menu-detail-page', args=[form.id]))
        return render(request, 'menu/new-menu-form.html', {'form':form})
