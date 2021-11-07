from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Doer


class DoerCreationForm(UserCreationForm):

    class Meta:
        model = Doer
        fields = ('email', 'first_name', 'last_name', 'password')

class DoerChangeForm(UserChangeForm):

    class Meta:
        model = Doer
        fields = ('first_name', 'last_name',)


