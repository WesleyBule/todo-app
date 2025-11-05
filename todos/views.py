from django.shortcuts import render , redirect
from .models import Todo
from datetime import datetime
from .forms import UserRegisterForm , TodoRegisterForm ,TodoEditForm
from django.http import JsonResponse


def user_register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request , 'todos/register.html' , context ) 

def todo_list(request):
    todos = Todo.objects.all()
    template_name = 'todos/home.html'
    return render(request,template_name ,{'todos':todos})

def todo_create(request):
    form = TodoRegisterForm()
    template_name = 'todos/create.html'
    if request.method == "POST":
        form = TodoRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoList')
    context = {'form':form}
    return render(request,template_name ,context)


def todo_edit(request , id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        form = TodoEditForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todoList")
    form = TodoEditForm(request.POST , instance=todo)
    return render(request , "todos/edit.html", {"form":form})


def todo_complete(request , id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todoList')

def todo_delete(request , id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todoList')


