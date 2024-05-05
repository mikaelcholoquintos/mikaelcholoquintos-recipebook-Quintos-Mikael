from django import form
from .models import Recipe, RecipeImage

class RecipeForm(form.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']

class RecipeImageForm(form.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']
