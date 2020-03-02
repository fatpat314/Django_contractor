from django.urls import include, path
from menu.views import MenuListView
from . import views

urlpatterns = [
    path('menu/', views.MenuListView.as_view(), name='menu-list'),
]
