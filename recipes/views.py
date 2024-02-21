from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe

# Create your views here.

def home(request):
   return render(request, 'recipes/home.html')

class RecipeListView(ListView):         #class-based view
   model = Recipe                       #specify model
   template_name = 'recipes/main.html'  #specify template 

class RecipeDetailsView(DetailView):      
   model = Recipe                     
   template_name = 'recipes/details.html'   