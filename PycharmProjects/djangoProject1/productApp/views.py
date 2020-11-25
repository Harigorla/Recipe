from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import ProductModel
from .forms import ProductForm


def ProductHome(request):
    public = ProductModel.objects.order_by('productname')
    return render(request, 'producthome.html', {'public': public})


def ProductCreate(request):
    if request.method == "POST":
        pform = ProductForm(request.POST)
        if pform.is_valid():
            productname = request.POST.get('productname','')
            productprice = request.POST.get('productprice','')
            productdetails = request.POST.get('productdetails','')
            data = ProductModel(
                productname=productname,
                productprice=productprice,
                productdetails=productdetails,
            )
            data.save()
            return HttpResponse('save')
    pform = ProductForm()
    return render(request, 'productcreate.html', {'pform': pform})


def detail(request, id):
    private = get_object_or_404(ProductModel, pk=id)
    return render(request, 'detail.html', {'private':private})