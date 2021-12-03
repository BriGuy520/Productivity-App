from django.db import models
from django.conf import settings

# Create your models here.

class NutritionData(models.Model):
    
    doer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

        
    serving_size = models.IntegerField
    calories = models.IntegerField
    fat = models.IntegerField
    protein = models.IntegerField
    carbs = models.IntegerField
