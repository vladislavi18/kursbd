from django.contrib import admin
from .models import Task, GroupTasks

admin.site.register(Task)
admin.site.register(GroupTasks)
