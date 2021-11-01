from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .models import Task

from .forms import ToDoListForm

# Create your views here.

def index(request):

    if request.method == "POST":

      form = ToDoListForm(request.POST)

      if form.is_valid():

        obj = Task()

        obj.task_title = form.cleaned_data['task_title']
        obj.task_summary = form.cleaned_data['task_summary']
        obj.save()

        return HttpResponseRedirect('task')

    else:
      form = ToDoListForm()
    
    return render(request, 'index.html', {'form': form})

def task(request):

  task_list = Task.objects.all()

  return render(request, 'task.html', {'task_list': task_list})

