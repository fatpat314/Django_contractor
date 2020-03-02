from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

from menu.models import MenuItem


# Create your views here.
class MenuListView(ListView):
    """Render List of Menu Items"""
    model = MenuItem

    def get(self, request):
        """Get a list of menu Items"""
        items = self.get_queryset().all()
        return render(request, 'menu-list.html', {
        'items':items
        })

class MenuDetailView(DetailView):
    """ render a specific menu item based on its slug"""
    model = MenuItem

    def get (self, request, slug):
        item = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'menu-page.html',{
        'item':item
        })
