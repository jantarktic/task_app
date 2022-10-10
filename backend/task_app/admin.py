from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'due_date', 'completed', 'status')

# Register your models here.

admin.site.register(Task, TaskAdmin)
