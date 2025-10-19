from django.shortcuts import render, redirect
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