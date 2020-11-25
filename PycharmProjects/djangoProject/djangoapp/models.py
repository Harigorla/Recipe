from django.db import models


class MenuName(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    process = models.TextField()
