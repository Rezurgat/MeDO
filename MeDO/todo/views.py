from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('tasks')