from django.urls import include, path
from event_planner.views import EventListView, EventDetailView, New_event_form

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('form/', New_event_form.as_view(), name='new'),
    path('<str:slug>/', EventDetailView.as_view(), name='event-details-page'),
    
]
