from django.shortcuts import render

# Create your views here.
# sales/views.py


def home(request):
    return render(request, "recipe/recipes_home.html")
