from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import DoerCreationForm, DoerChangeForm
from .models import Doer

# Register your models here.

class CustomUserAdmin(UserAdmin):
  add_form = DoerCreationForm
  form = DoerChangeForm
  model = Doer
  list_display = ['email', 'username',]

admin.site.register(Doer, CustomUserAdmin)



