from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/ingredient/{}/".format(self.pk)

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/recipe/{}/".format(self.pk)

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
