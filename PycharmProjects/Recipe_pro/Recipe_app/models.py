from django.db import models

class Recipe (models.Model):
   name = models.CharField(max_length=255)

class Items_list (models.Model):
    ingredients = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    Process = models.TextField()

