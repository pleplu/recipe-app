from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailsView

app_name = 'recipes'  

urlpatterns = [
   path('', home, name='home'),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailsView.as_view(), name='details'),
]