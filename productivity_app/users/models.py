from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager

# Create your models here.

class Doer(AbstractUser):
  
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField(max_length=100)


  def __str__(self):
    return f'{self.first_name} {self.last_name}'



