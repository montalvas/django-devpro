from django import forms
from .models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'done']