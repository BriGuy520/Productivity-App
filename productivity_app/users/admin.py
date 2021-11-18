from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Doer

# Register your models here.
class AddDoerForm(forms.ModelForm):

  password1 = forms.CharField(
    label='Password', widget=forms.PasswordInput
  )

  password2 = forms.CharField(
    label = 'Confirm password', widget=forms.PasswordInput
  )

  class Meta:
    model = Doer
    fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')

      if password1 and password2 and password1 is not password2:
        raise forms.ValidateForm("Passwords do not match")
      return password2
    
    def save(self, commit=True):

      user = super().save(commit=False)
      user.set_password(self.cleaned_data['password1'])

      if commit:
        user.save()
      return user

class UpdateDoerForm(forms.ModelForm):

  password = ReadOnlyPasswordHashField()

  class Meta: 
    model = Doer
    fields = (
      'email', 'first_name', 'last_name', 'is_active', 'is_staff',
    )

  def clean_password(self):
    return self.initial['password']


class UserAdmin(BaseUserAdmin):

  form = UpdateDoerForm
  add_form = AddDoerForm

  list_display = ('email', 'first_name', 'last_name', 'is_staff',)
  list_filter = ('is_staff',)

  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal info', {'fields': ('first_name', 'last_name')}),
    ('Permissions', {'fields': ('is_active', 'is_staff')}),
  )

  add_fieldsets = (
    (
      None,
      {
        'classes':('wide',),
        'fields': (
          'email', 'first_name', 'last_name', 'password1', 'password2',
        )
      }
    ),
  )

  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', 'first_name', 'last_name')
  filter_horizontal = ()
  
admin.site.register(Doer, UserAdmin)


