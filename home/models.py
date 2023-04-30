from django.db import models
from django.forms import ModelForm


class ToDoModel(models.Model):
    toDoItem = models.TextField(verbose_name='toDo')
    toDoStatus = models.ForeignKey('StatusModel', default=1, on_delete=models.PROTECT, verbose_name='status')
    toDoAction = models.BooleanField(default=False, verbose_name='buttons')


class StatusModel(models.Model):
    toDoStatus = models.CharField(max_length=255, verbose_name='status')

    def __str__(self):
        return self.toDoStatus

