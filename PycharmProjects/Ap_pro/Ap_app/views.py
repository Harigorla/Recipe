from django.shortcuts import render , get_object_or_404
from .models import TsModel,TsChoice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    x = TsModel.objects.order_by('pub_date')[:5]
    return render(request,'index.html',{'x': x})

def detail(request,TsModel_id):

    tsmodel=TsModel.objects.get(pk=TsModel_id)
    return render(request,'detail.html',{'tsmodel':tsmodel})
