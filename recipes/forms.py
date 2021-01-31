from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Recipe, Tag



class RecipeForm(ModelForm):
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                    to_field_name='tag')

    class Meta:
        model = Recipe
        fields = ['title', 'time', 'description', 'image']