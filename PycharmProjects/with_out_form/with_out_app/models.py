from django.db import models

class Wmodel(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()

