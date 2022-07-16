from django.shortcuts import render, HttpResponse
from .models import Recipe

# Create your views here.
def home(request):
    r = Recipe.objects.all()
    context = {
        "recipies": r,
    }
    return render(request, 'home.html', context)

def recipe_detail(request, id):
    
    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return HttpResponse("Wrong Number")
    context = {
        "recipe": recipe,
    }
    return render(request, 'recipe.html', context)