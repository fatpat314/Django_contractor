from django.urls import include, path
from event_planner.views import EventListView, EventDetailView, New_event_form, EventDeleteView
from . import views


urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('form/', New_event_form.as_view(), name='new'),
    path('<str:slug>/', EventDetailView.as_view(), name='event-details-page'),
    path('<str:slug>/edit/', views.EventEditView.as_view(), name='event-edit-page'),
    path('<str:slug>/delete/', views.EventDeleteView.as_view(), name='event-delete-page')

]
# <str:slug>
