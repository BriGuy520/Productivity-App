from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import DoerCreationForm

# Create your views here.

def user_profile(request):

  render(request, 'user.html')

class SignUpView(CreateView):
  form_class = DoerCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

