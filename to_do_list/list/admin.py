from django.contrib import admin

from .models import Task, Doer

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  model = Task

@admin.register(Doer)
class DoerAdmin(admin.ModelAdmin):
  model = Doer





