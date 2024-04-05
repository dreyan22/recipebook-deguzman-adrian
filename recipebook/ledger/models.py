from django.db import models
from django.urls import reverse, reverse_lazy
from accounts.models import Profile


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])
    

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
   
    def __str__(self):
        return f'{self.quantity} : {self.ingredient.name}'
    

class RecipeImage(models.Model):
    recipe_image = models.ImageField(upload_to='images/', 
null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_images')

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.kwargs['pk']])