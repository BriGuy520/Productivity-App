from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect

from .models import Task

from .forms import ToDoListForm

# Create your views here.

def add_task(request):

    if request.method == "POST":

      form = ToDoListForm(request.POST)

      if form.is_valid():

        save_task = form.save(commit=False)
        save_task.doer = request.user

        save_task.save()

        return redirect('task')

    else:
      form = ToDoListForm()
    
    return render(request, 'add_task.html', {'form': form})

@login_required
def task(request):


  task_list = Task.objects.filter(doer=request.user)

  return render(request, 'task.html', {'task_list': task_list})


class DeleteTask(DeleteView):
  model = Task
  template_name_suffix = '_delete_form'
  success_url = reverse_lazy('task')

class UpdateTask(UpdateView):
  model = Task

  fields = ['task_title', 'task_summary']
  template_name_suffix = '_update_form'
  success_url = reverse_lazy('task')


