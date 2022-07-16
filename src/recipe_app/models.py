from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=256) #max_length mandatory
    ingredients = models.TextField()
    procedure = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
