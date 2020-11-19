
from django.db import models

class EmpModel(models.Model):
    Ename=models.CharField(max_length=200)
    Eid=models.IntegerField()
    Email=models.EmailField()

