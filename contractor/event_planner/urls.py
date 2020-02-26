from django.urls import include, path
from event_planner.views import EventListView

urlpatterns = [
    path('', EventListView.as_view(), name='event-list')
]
