from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecipeForm
from .models import Recipe, Tag, Quantity, Ingredient, User


def index(request):
    recipes_list = Recipe.objects.all().order_by('-pub_date')
    paginator = Paginator(recipes_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, }
    )


def found_ingredient(request):
    query = request.GET.get("query").lower()[:-1]
    ingredients = Ingredient.objects.filter(
        title__icontains=query).values("title", "dimension").order_by('title')
    return JsonResponse(list(ingredients), safe=False)


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

        for ingredient, value in ingredients.items():
            Quantity.objects.create(ingredient=ingredient,
                                  recipe=recipe,
                                  amount=value)
        return redirect('index')
    return render(request, 'new.html', {'form': form})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipes = author.recipes.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    # following = author.following.count()
    # subscriptions = author.follower.count()
    return render(request, "profile.html", {"author": author,
                                            "count":paginator.count,
                                            "page": page,
                                            "recipes": recipes,
                                            "paginator": paginator
                                            })


def recipe_view(request, username, recipe_id):
    """Просмотр одного поста."""
    recipe = get_object_or_404(Recipe, id=recipe_id, author__username=username)
    form = RecipeForm(request.POST or None)
    author = recipe.author
    # following = author.following.count()
    # subscriptions = author.follower.count()
    return render(request, "recipe_view.html", {
        "recipe": recipe,
        "author": author,
        "form": form,
    })
    # "following": following,
    # "subscriptions": subscriptions