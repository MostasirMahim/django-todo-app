from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markComplete/<int:todo_id>/', views.markComplete, name='markComplete'),
    path('markUnComplete/<int:todo_id>/', views.markUnComplete, name='markUnComplete'),
    path('editTask/<int:todo_id>/', views.updatetask, name='editTask'),
    path('deleteTask/<int:todo_id>/', views.deleteTask, name='deleteTask'),
]