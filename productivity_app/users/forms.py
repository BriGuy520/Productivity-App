from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Doer


class DoerCreationForm(UserCreationForm):

    class Meta:
        model = Doer
        fields = ('email', 'first_name', 'last_name')

        def save(self, commit=True):
            user = super(DoerCreationForm, self.save(commit=False))

            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

class DoerChangeForm(UserChangeForm):

    class Meta:
        model = Doer
        fields = ('first_name', 'last_name',)

class DoerLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, *kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'my-password'
        })

