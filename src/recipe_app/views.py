from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hello")
    return render(request, 'home.html')

def recipe_detail(request, id):
    return render(request, 'recipe.html')