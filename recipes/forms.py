from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Recipe, Tag



class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'time', 'description', 'image', 'tags']

        widgets = {'tags': forms.CheckboxSelectMultiple()}