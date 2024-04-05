from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeInline, RecipeImageInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)