from django.urls import path
from .views import *


urlpatterns = [
    path('home/', index, name='Home'),
    path('addTodoItem/', addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('doneToDoItem/<int:i>/', doneToDoView),
]