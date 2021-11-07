from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth import get_user_model

from django.http import HttpResponse, HttpResponseRedirect

from .forms import DoerCreationForm


# Create your views here.
def add_user(request):

  if request.method == "POST":
    
    form = DoerCreationForm(request.POST)

    if form.is_valid():

      form.save()

      return HttpResponseRedirect('/')

    else:
      form = DoerCreationForm()
      
    return render(request, 'add_user.html', {'form': form})



def user_profile(request):

  Doer = get_user_model()

  return render(request, 'user_profile.html', {'users': Doer.objects.all()})