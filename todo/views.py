from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.


def addTask(request):
    print(request.POST['task'])
    task = request.POST['task']
    Todo.objects.create(title=task)
    return redirect('home')
