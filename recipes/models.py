from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=60)

    ingredients = models.CharField(max_length=300, help_text='seperated by a comma')

    cooking_time = models.FloatField(help_text='in minutes')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')

        if self.cooking_time < 30 and len(ingredients) < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 30 and len(ingredients) >= 7:
            difficulty = 'Medium'
        elif self.cooking_time >= 30 and len(ingredients) < 7:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 30 and len(ingredients) >= 7:
            difficulty = 'Hard'
        return difficulty

    def __str__(self):
        return str(self.name)