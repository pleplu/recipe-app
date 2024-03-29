from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm

# Create your tests here.

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea-leaves, water, sugar')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name, 'name')

    def test_ingredients_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_ingredients = recipe._meta.get_field('ingredients').help_text
        self.assertEqual(recipe_ingredients, 'seperated by a comma')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cooking_time, 'in minutes')

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Easy')

    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
    #    get_absolute_url() should take you to the detail page of recipe #1
    #    and load the URL /recipes/list/1
       self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipesSearchFormTest(TestCase):

    def test_renders_chart_type(self):
        form = RecipesSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_valid_data(self):
        form = RecipesSearchForm(
            data={'recipe_name': 'Tea', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())