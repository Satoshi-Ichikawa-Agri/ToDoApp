from django.contrib import admin
from django.urls import path

from TodoApp.views import *


urlpatterns = [
    path('', todo_views.TopPageView.as_view(), name='home'),
    path('index/', todo_views.TodoIndexView.as_view(), name='index'),
    path('details/<str:pk>/', todo_views.TodoDetailView.as_view(), name='details'),
    path('create/', todo_views.TodoCreateView.as_view(), name='create'),
    path('edit/<str:pk>/', todo_views.TodoEditView.as_view(), name='edit'),
    path('delete/<str:pk>/', todo_views.TodoDeleteView.as_view(), name='delete'),
]
