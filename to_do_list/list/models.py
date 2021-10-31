from django.db import models

import uuid

# Create your models here.

class User(models.Model):

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  


class Task(models.Model):
  
  task_title = models.CharField(max_length=100)
  task_summary = models.TextField(max_length=1000)

