from django.db import models

class TsModel(models.Model):
    q_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")

class TsChoice(models.Model):
    tsmodel=models.ForeignKey(TsModel,on_delete=models.CASCADE)
    c_text=models.CharField(max_length=300)
    votes=models.IntegerField(default=0)


