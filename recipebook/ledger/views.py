from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .models import Recipe
from .forms import RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = RecipeForm()
        return ctx

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_create.html'
    login_url = '/accounts/login/'

    # def get_success_url(self):
    #     return reverse_lazy('recipe/add', kwargs={ 'pk': self.object.pk })
    
    
class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_detail.html'
    