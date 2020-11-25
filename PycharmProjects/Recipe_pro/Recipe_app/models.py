from django.db import models


class NameList(models.Model):
    name = models.CharField(max_length=300)
    ingredients = models.TextField()
    Process = models.TextField()
