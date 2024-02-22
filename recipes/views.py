from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_recipe_name_from_id, get_chart

# Create your views here.

def home(request):
   return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):   #class-based view
   model = Recipe                       #specify model
   template_name = 'recipes/main.html'  #specify template 

class RecipeDetailsView(LoginRequiredMixin, DetailView):      
   model = Recipe                     
   template_name = 'recipes/details.html'   

@login_required
def records(request):
      form = RecipesSearchForm(request.POST or None)

      recipe_df = None
      recipe_name = None
      chart = None

      if request.method == 'POST':
         recipe_name = request.POST.get('recipe_name')
         chart_type = request.POST.get('chart_type')

         qs = Recipe.objects.filter(name=recipe_name)

         if qs:
            recipe_df = pd.DataFrame(qs.values())
            recipe_df['id']=recipe_df['id'].apply(get_recipe_name_from_id)
            chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)
            recipe_df = recipe_df.to_html()

      context = {
         'form': form,
         'recipe_df': recipe_df,
         'recipe_name': recipe_name,
         'chart': chart,
      }

      return render(request, 'recipes/search.html', context)