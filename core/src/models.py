
from django.db import models
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
      return self.category_name
class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    recipe_name = models.CharField(max_length=100)
    recipe = models.TextField()
    def __str__(self):
      return self.recipe_name
