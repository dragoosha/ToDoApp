from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


def index(request):
    items = ToDoModel.objects.all()
    context = {
        'items': items,
        'title': 'Home',
    }
    return render(request, 'home/index.html', context=context)


def addTodoView(request):
    x = request.POST['ToDo']
    new_item = ToDoModel(toDoItem=x)
    new_item.save()
    return HttpResponseRedirect('/home')


def deleteTodoView(request, i):
    y = ToDoModel.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/home/')


def doneToDoView(request, i):
    z = ToDoModel.objects.get(id=i)
    z.toDoStatus_id = 2
    z.save()
    return HttpResponseRedirect('/home/')
