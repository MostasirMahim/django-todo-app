
from django.shortcuts import render
from todo.models import Todo
def home(request):
    incomplete_task = Todo.objects.filter(is_completed=False).order_by('-created_at')
    completed_task = Todo.objects.filter(is_completed=True)
    print(incomplete_task)
    context = {
        'incomplete_task': incomplete_task,
        'completed_task': completed_task
    }
    return render(request, 'home.html', context)