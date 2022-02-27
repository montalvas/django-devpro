from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField('Tarefa', max_length=128)
    done = models.BooleanField(default=False)
