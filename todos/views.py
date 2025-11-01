from django.shortcuts import render , redirect
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    template_name = 'todos/home.html'
    return render(request,template_name ,{'todos':todos})

def todo_create(request):
    template_name = 'todos/create.html'
    if request.method == "POST":
        title = request.POST.get('title')
        created = request.POST.get('created')
        deadline = request.POST.get('deadline')
        completed = request.POST.get('completed')

        Todo.objects.create(
            title=title,
            created = created,
            deadline = deadline,
            completed = completed
        )
        return redirect('todoList')
    return render(request,template_name)