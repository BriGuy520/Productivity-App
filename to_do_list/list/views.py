from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Task

from .forms import ToDoListForm

# Create your views here.

def index(request):

    if request.method == "POST":

      form = ToDoListForm(request.POST)

      if form.is_valid():

        # obj = Task()

        # obj.task_title = form.cleaned_data['task_title']
        # obj.task_summary = form.cleaned_data['task_summary']
        # obj.save()

        form.save()

        return HttpResponseRedirect('task')

    else:
      form = ToDoListForm()
    
    return render(request, 'index.html', {'form': form})

def task(request):

  task_list = Task.objects.all()

  return render(request, 'task.html', {'task_list': task_list})

def delete_task(request, pk):
  task_to_delete = Task.objects.get(pk=pk)
  task_to_delete.delete()
  return render(request, 'task/')


