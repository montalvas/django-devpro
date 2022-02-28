from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from task.models import Task
from .forms import NewTaskForm, TaskForm


def home(request):
    pending_tasks = Task.objects.filter(done=False).all()
    done_tasks = Task.objects.filter(done=True).all()
    context = {
        'pending_tasks': pending_tasks,
        'done_tasks': done_tasks,
        }
    
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:home'))
        else:
            context.update({'form': form})
            return render(request, 'task/home.html', context, status=400)
    
    return render(request, 'task/home.html', context)

def update(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse('task:home'))

def delete(request, task_id):
    if request.method == 'POST':
        Task.objects.filter(id=task_id).delete()

    return HttpResponseRedirect(reverse('task:home'))
