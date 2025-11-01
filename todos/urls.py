from django.urls import path
from . import views
urlpatterns = [
    path('',views.todo_list , name='todoList'),
    path('add/', views.todo_create , name='todoCreate'),
]