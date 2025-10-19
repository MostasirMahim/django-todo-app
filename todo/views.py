from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo

# Create your views here.


def addTask(request):
    print(request.POST['task'])
    task = request.POST['task']
    Todo.objects.create(title=task)
    return redirect('home')

def markComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.is_completed = True
    todo.save()
    return redirect('home')

def markUnComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.is_completed = False
    todo.save()
    return redirect('home')

def updatetask(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == 'POST':
        new_task = request.POST['newtask']
        todo.title = new_task
        todo.save()
        return redirect("home")
    else:
        context = {
            "todo" : todo
        }
        return render(request, "edit_todo.html", context)

def deleteTask(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('home')