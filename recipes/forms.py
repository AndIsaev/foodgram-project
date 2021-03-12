from django import forms
from .models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        to_field_name='title'
    )

    class Meta:
        model = Recipe
        fields = ['title', 'time', 'description', 'image', 'ingredients']
