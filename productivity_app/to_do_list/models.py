from django.db import models
from django.forms import ModelForm

import uuid

# Create your models here.

class Doer(models.Model):

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  


class Task(models.Model):
  
  task_title = models.CharField(max_length=100)
  task_summary = models.TextField(max_length=1000)

  STATUS = (
    ('NOT_STARTED', 'Not Started'),
    ('IN_PROGRESS', 'In Progress'),
    ('FINISHED', 'Finished'), 
  )

  task_status = models.CharField(max_length=12, choices=STATUS, default='NOT_STARTED')

  doer = models.ForeignKey('Doer', on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.task_title
  
