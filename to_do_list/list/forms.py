from django.forms import ModelForm
from .models import Task

class ToDoListForm(ModelForm):
  
  class Meta:
    model = Task
    
    fields = ('task_title', 'task_summary')

