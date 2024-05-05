from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    update_on = models.DateTimeField(auto_now=True)

class RecipeDetail(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    details = models.TextField()