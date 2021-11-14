from django.db import models

# Create your models here.

class NutritionData(models.Model):

    calories = models.IntegerField
    fat = models.IntegerField
    protein = models.IntegerField
    carbs = models.IntegerField
