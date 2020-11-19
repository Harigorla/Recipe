from django.shortcuts import render
from django.http import HttpResponse
from .forms import Wform
from .models import Wmodel

# def Wview(request):
#
#     return render(request,'wform.html')
def Wview(request):

    if request.method == "POST":
        form=Wform(request.POST)

        if form.is_valid():
           return HttpResponse('Data inserted')
        else:
            return HttpResponse('Data  not inserted')
    else:
        form=Wform()
        return render(request,'wform1.html',{'abc':form})
