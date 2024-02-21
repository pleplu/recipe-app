from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=60)

    ingredients = models.CharField(max_length=300, help_text='seperated by a comma')

    cooking_time = models.FloatField(help_text='in minutes')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')

        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        return difficulty
    
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
       return reverse('recipes:details', kwargs={'pk': self.pk})