from django.shortcuts import render , redirect
from .models import Todo
from datetime import datetime
from .forms import UserRegisterForm , TodoRegisterForm

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