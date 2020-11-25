from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import MenuName
from .forms import MenuForm


def home(request):
    menu_list = MenuName.objects.order_by('name')
    return render(request, 'menu.html', {'menu_list': menu_list})


def detail(request, id):
    menu =get_object_or_404(MenuName, pk=id)
    return render(request, 'detail.html', {'menu': menu})
