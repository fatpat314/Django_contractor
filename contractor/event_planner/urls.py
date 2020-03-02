from django.urls import include, path

from event_planner.views import EventListView, EventDetailView, New_event_form, EventDeleteView, SearchResultsView
from menu.views import MenuListView
from . import views
# from menu.views import views


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', EventListView.as_view(), name='event-list'),
    path('form/', New_event_form.as_view(), name='new'),
    path('<str:slug>/', EventDetailView.as_view(), name='event-details-page'),
    path('<str:slug>/edit/', views.EventEditView.as_view(), name='event-edit-page'),
    path('<str:slug>/delete/', views.EventDeleteView.as_view(), name='event-delete-page'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('menu/', MenuListView.as_view(), name='menu-list'),



]
# <str:slug>
