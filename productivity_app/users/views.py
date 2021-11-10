from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth import get_user_model, login

from django.http import HttpResponse, HttpResponseRedirect

from .forms import DoerCreationForm, DoerLoginForm


# Create your views here.
def add_user(request):

  if request.method == "POST":
    
    form = DoerCreationForm(request.POST)

    if form.is_valid():

      user = form.save()

      login(request, user)

      return redirect('/user/')

  else:
    form = DoerCreationForm()
    
  return render(request, 'add_user.html', {'form': form})



def user_profile(request):

  Doer = get_user_model()

  return render(request, 'user_profile.html', {'users': Doer.objects.all()})

def user_login(request):

  if request.method == 'POST':

    form = DoerLoginForm

    if form.is_valid():

      pass

  else:

    form = DoerLoginForm
  
  return render(request, 'user_login.html', {'form': form})