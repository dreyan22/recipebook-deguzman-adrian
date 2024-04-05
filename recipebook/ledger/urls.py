from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeImageCreateView


urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='create'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view(), name='recipeimage_create'),
]


app_name = 'ledger'