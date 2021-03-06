from django.db import models
from django.conf import settings
from django.forms import ModelForm

import uuid

# Create your models here.

class Task(models.Model):

  doer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
  
  task_title = models.CharField(max_length=100)
  task_summary = models.TextField(max_length=1000)

  STATUS = (
    ('NOT_STARTED', 'Not Started'),
    ('IN_PROGRESS', 'In Progress'),
    ('FINISHED', 'Finished'), 
  )

  task_status = models.CharField(max_length=12, choices=STATUS, default='NOT_STARTED')

  def __str__(self):
    return self.task_title
  

