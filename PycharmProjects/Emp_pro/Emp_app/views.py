from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpForm

def Home(request):

    if request.method == "POST":

        aform=EmpForm(request.POST)

        if aform.is_valid():
            aform.save()
            return HttpResponse('save')
    else:
        aform=EmpForm()
        return render(request,'form.html',{'aform':aform})
