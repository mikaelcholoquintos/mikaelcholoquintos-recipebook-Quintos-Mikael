from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage

@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipebook:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipebook/recipe_add.html', {'form': form})

@login_required
def recipe_add_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('recipebook:recipe_detail', pk=pk)
    else:
        form = RecipeImageForm()
    return render(request, 'recipebook/recipe_add_image.html', {'form': form})
