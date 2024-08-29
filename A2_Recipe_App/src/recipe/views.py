from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"  # Update the template name


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"
    context_object_name = "recipes"


def home(request):
    return render(request, "recipe/home.html", {"recipe": recipe_list})


def recipe_list(request):
    recipes = Recipe.objects.all()  # Add the namespace here
    return render(request, "recipes.html", {"recipes": recipes})


def recipe_detail(request):
    return render(request, "recipe/recipe_detail.html")
