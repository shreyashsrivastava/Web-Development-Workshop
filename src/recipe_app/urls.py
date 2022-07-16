from django.urls import path
from . import views

app_name = 'recipe_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/<int:id>', views.recipe_detail, name="recipe-detail")
]