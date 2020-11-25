from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import NameList
from .forms import NameForm
from django.urls import reverse


def home(request):
    order_list = NameList.objects.order_by('name')
    return render(request, 'home.html', {'order_list': order_list})


def recipe(request):
    if request.method == "POST":
        rform = NameForm(request.POST)
        if rform.is_valid():
            name = request.POST.get('name', '')
            data = NameList(name=name)
            data.save()
            return HttpResponseRedirect('home.html')
        else:
            return HttpResponse('Not save')
    else:
        rform = NameForm()
        return render(request, 'recipe.html', {'fform': rform})


def details(request, id):
    order_list = NameList.objects.get(pk=id)
    return render(request, 'details.html', {'order_list': order_list})


def results(request, recipe):
    recipe = get_object_or_404(NameList, pk=NameList)
    try:
        select_choice = get_object_or_404(pk=request.POST['choice'])
    except(KeyError, get_object_or_404):
        return render(request, 'details.html', {'recipe': recipe})
    else:
        select_choice.Process += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('recipe', args=(recipe.name,)))
