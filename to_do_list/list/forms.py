from django import forms

class ToDoListForm(forms.Form):
  task_title = forms.CharField(label='Task Title', max_length=100)
  task_summary = forms.CharField(widget=forms.Textarea(), label='Task Details', max_length=1000)

  def clean(self):

    cleaned_data = super(ToDoListForm, self).clean()
    task_title = cleaned_data.get('task_title')
    task_summary = cleaned_data.get('task_summary')

    if not task_title and not task_summary:
      raise forms.ValidationError("Error!")