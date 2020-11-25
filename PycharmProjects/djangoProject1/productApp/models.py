from django.db import models


class ProductModel(models.Model):
    productname = models.CharField(max_length=500)
    productprice = models.CharField(max_length=200)
    productdetails = models.TextField()
