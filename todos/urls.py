from django.urls import path
from . import views
urlpatterns = [
    path('',views.todo_list , name='todoList'),
    path('add/', views.todo_create , name='todoCreate'),
    path('register/',views.user_register , name='userRegister'),
    path('complete/<int:id>/', views.todo_complete, name='todoComplete'),
    path('delete/<int:id>/', views.todo_delete, name='todoDelete'),
    path('edit/<int:id>',views.todo_edit , name="todoEdit"),
]