from django.db import models

import uuid

# Create your models here.

class User(models.Model):

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  


class Task(models.Model):
  
  task_title = models.CharField(max_length=100)
  task_summary = models.TextField(max_length=1000)
  task_status = models.CharField(max_length=3)



