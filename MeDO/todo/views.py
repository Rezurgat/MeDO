from django.views.generic import ListView

from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

