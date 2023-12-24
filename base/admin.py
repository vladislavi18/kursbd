from django.contrib import admin
from .models import Task, GroupTasks, Board

admin.site.register(Task)
admin.site.register(GroupTasks)
admin.site.register(Board)

