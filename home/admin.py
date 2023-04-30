from django.contrib import admin
from .models import *


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('toDoItem', 'toDoStatus', 'toDoAction')
    list_display_links = ('toDoStatus', 'toDoAction')
    search_fields = ('toDoItem',)
    list_filter = ('toDoStatus',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'toDoStatus')


admin.site.register(ToDoModel, ToDoAdmin)
admin.site.register(StatusModel, StatusAdmin)
