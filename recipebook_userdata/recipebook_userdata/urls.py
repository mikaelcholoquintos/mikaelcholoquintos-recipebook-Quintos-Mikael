from django.urls import path
from . import views

app_name = 'recipebook'

urlpatterns = [
    path('add/', views.recipe_add, name='recipe_add'),
    path('<int:pk>/add_image/', views.recipe_add_image, name='recipe_add_image'),
]
