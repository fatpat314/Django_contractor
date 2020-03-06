from django.urls import include, path

from event_planner.views import EventListView, EventDetailView, New_event_form, EventEditView, EventDeleteView, SearchResultsView
from menu.views import MenuListView, MenuDetailView, MenuCreateView, MenuEditView, MenuDeleteView
from . import views

# from menu.views import views


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', EventListView.as_view(), name='event-list'),
    path('form/', New_event_form.as_view(), name='new'),
    path('<int:id>/', EventDetailView.as_view(), name='event-details-page'),
    path('<str:slug>/edit/', views.EventEditView.as_view(), name='event-edit-page'),
    path('<int:id>/delete/', views.EventDeleteView.as_view(), name='event-delete-page'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('new-menu/', MenuCreateView.as_view(), name='new-menu-item'),
    path('<int:id>/menu-details/', MenuDetailView.as_view(), name='menu-detail-page'),
    path('<int:pk>/menu-edit/', MenuEditView.as_view(), name='menu-edit-page'),
    path('<int:pk>/menu-delete/', MenuDeleteView.as_view(), name='menu-delete-page')



]
# <str:slug>
