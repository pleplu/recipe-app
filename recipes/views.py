from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
   return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):   #class-based view
   model = Recipe                       #specify model
   template_name = 'recipes/main.html'  #specify template 

class RecipeDetailsView(LoginRequiredMixin, DetailView):      
   model = Recipe                     
   template_name = 'recipes/details.html'   