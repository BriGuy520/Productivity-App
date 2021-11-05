from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager

# Create your models here.

class Doer(AbstractUser):
    
    pass
    

    def __str__(self):
        return self.username




