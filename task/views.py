from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import NewTaskForm


def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:home'))
        else:
            return render(request, 'task/home.html', {'form': form}, status=400)

    return render(request, 'task/home.html')
