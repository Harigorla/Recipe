from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Recipe,Items_list
from .forms import RecipeForm
from django.urls import reverse
def Home(request):

    order_list = Recipe.objects.order_by('name')
    return render(request , 'home.html', {'order_list':order_list})


def RecipeView(request):

    if request.method == "POST":
        rform = RecipeForm(request.POST)
        if rform.is_valid():
            name=request.POST.get('name','')
            data=Recipe(name=name)
            data.save()
            return HttpResponseRedirect('home.html')
        else:
            return HttpResponse('Not save')
    else:
        rform = RecipeForm()
        return render(request, 'recipe.html',{'fform': rform})

def details(request ,id):

    recipe = Recipe.objects.get(pk=Recipe)
    return render(request,'details.html',{'recipe':recipe},id)

def results(request,recipe):

    recipe = get_object_or_404(Recipe,pk=Recipe)
    try:
        select_choice = recipe.items_list_set.get(pk=request.POST['choice'])
    except(KeyError, Items_list.DoesNotExist):
        return render(request,'details.html',{'recipe':recipe})
    else:
        select_choice.Process+=1
        select_choice.save()
        return HttpResponseRedirect(reverse('recipe',args=(recipe.name,)))
