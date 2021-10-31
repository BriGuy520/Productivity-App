from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from list.forms import ToDoListForm

# Create your views here.

def index(request):
  if request.method == 'POST':

    form = ToDoListForm(request.POST)

    if form.is_valid():
      pass
    else:
      form = ToDoListForm()
    
    return render(request, 'index.html', {'form': form})
