from django.shortcuts import render
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    template_name = 'todos/home.html'
    return render(request,template_name ,{'todos':todos})
