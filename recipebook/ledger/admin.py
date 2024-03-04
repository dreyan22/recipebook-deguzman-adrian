from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]


admin.site.register(Recipe, RecipeAdmin)