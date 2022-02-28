from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from task.models import Task
from .forms import NewTaskForm


def home(request):
    pending_tasks = Task.objects.all()
    context = {'pending_tasks': pending_tasks}
    
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:home'))
        else:
            context.update({'form': form})
            return render(request, 'task/home.html', context, status=400)
    
    return render(request, 'task/home.html', context)
