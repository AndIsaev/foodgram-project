from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecipeForm
from .models import Recipe, Tag, Quantity, Ingredient




def index(request):
    recipes_list = Recipe.objects.all().order_by('-pub_date')
    paginator = Paginator(recipes_list, 1)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, }
    )



def get_dict_ingredient(request_obj):
    tmp = dict()
    for key in request_obj:
        if key.startswith('nameIngredient'):
            ingredient = get_object_or_404(Ingredient, title=request_obj[key])
            value = key[15:]
            tmp[ingredient] = request_obj['valueIngredient_' + value]
    return tmp


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        ingredients = get_dict_ingredient(request.POST)
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        recipe.tags.set(form.cleaned_data['tags'])
        # active_tags = list(recipe.tags.values_list('key', flat=True))

        for ingredient, value in ingredients.items():
            Quantity.objects.create(ingredient=ingredient,
                                  recipe=recipe,
                                  quantity=value)
        return redirect('index')
    return render(request, 'new.html', {'form': form})


# def create_recipe(request):
