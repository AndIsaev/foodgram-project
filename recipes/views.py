from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from foodgram.settings import PAGES, PAGES_SUBSCRIBE
from .forms import RecipeForm
from .models import (Recipe,
                     Tag, Quantity,
                     Ingredient, User,
                     Purchase)


def get_filters_recipes(request, *args, **kwargs):
    filters = request.GET.getlist("filters")
    if filters:
        recipes = Recipe.objects.filter(
            tags__title__in=filters).filter(**kwargs).distinct()
    else:
        recipes = Recipe.objects.filter(**kwargs).all()

    return filters, recipes


def index(request):
    """Return main page."""
    filters, recipes = get_filters_recipes(request)
    paginator = Paginator(recipes, PAGES)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    tags = Tag.objects.all()
    return render(
        request,
        "index.html",
        {"page": page,
         "paginator": paginator,
         "tags": tags,
         "filter": filters}
    )


def get_dict_ingredient(request_obj):
    tmp = dict()
    for key in request_obj:
        if key.startswith("nameIngredient"):
            ingredient = get_object_or_404(Ingredient,
                                           title=request_obj[key])
            value = key[15:]
            tmp[ingredient] = request_obj["valueIngredient_" + value]
    return tmp


@login_required
def new_recipe(request):
    """Create new recipe."""
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None)

    if form.is_valid():
        ingredients = get_dict_ingredient(request.POST)
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        recipe.tags.set(form.cleaned_data["tags"])

        for ingredient, value in ingredients.items():
            Quantity.objects.create(ingredient=ingredient,
                                    recipe=recipe,
                                    amount=value)
        return redirect("index")
    return render(
        request,
        "new.html",
        {"form": form,
         "title_text": "Добавить запись"}
    )


def profile(request, username):
    """Return view the author's profile and recipes."""
    author = get_object_or_404(User, username=username)
    filters, recipes = get_filters_recipes(request, author=author.id)
    tags = Tag.objects.all()
    paginator = Paginator(recipes, PAGES)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request,
                  "recipes/profile.html",
                  {"author": author,
                   "count": paginator.count,
                   "page": page,
                   "recipes": recipes,
                   "paginator": paginator,
                   "tags": tags,
                   "filter": filters}
                  )


def recipe_view(request, username, recipe_id):
    """Return view recipe."""
    recipe = get_object_or_404(Recipe,
                               id=recipe_id,
                               author__username=username)
    form = RecipeForm(request.POST or None)
    author = recipe.author
    ingredients = Quantity.objects.filter(recipe=recipe_id)
    return render(request, "recipes/recipe_view.html", {
        "recipe": recipe,
        "author": author,
        "form": form,
        "ingredients": ingredients}
                  )


@login_required
def recipe_edit(request, username, recipe_id):
    """Edit recipe."""
    recipe = get_object_or_404(Recipe,
                               id=recipe_id,
                               author__username=username)

    if recipe.author != request.user:
        return redirect("recipe_view",
                        username=username,
                        recipe_id=recipe_id)

    form = RecipeForm(request.POST or None,
                      files=request.FILES or None,
                      instance=recipe)
    if form.is_valid():
        ingredients = get_dict_ingredient(request.POST)
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        recipe.tags.set(form.cleaned_data["tags"])
        Quantity.objects.filter(recipe_id=recipe.id).delete()
        for ingredient, value in ingredients.items():
            Quantity.objects.create(
                ingredient=ingredient,
                recipe=recipe,
                amount=value)

        return redirect('recipe_view',
                        username=username,
                        recipe_id=recipe_id)

    ingredients = Quantity.objects.filter(recipe=recipe_id)
    tags = list(recipe.tags.values_list('title', flat=True))

    return render(request, "new.html", {
        "form": form,
        "recipe": recipe,
        "ingredients": ingredients,
        "tags": tags,
        "title_text": "Редактирование рецепта"}
                  )


@login_required
def delete_recipe(request, recipe_id, username):
    """Delete recipe."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
    return redirect("index")


@login_required
def favorites(request):
    """Return favorites recipe."""
    user = request.user
    filters, recipes = get_filters_recipes(request, favorites__user=user)
    tags = Tag.objects.all()
    paginator = Paginator(recipes, PAGES)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(request, "recipes/favorite.html", {
        "page": page,
        "paginator": paginator,
        "tags": tags,
        "filter": filters,
        "favorite": True, }
                  )


@login_required
def subscriptions(request):
    """Return subscriptions and recipes."""
    user = request.user
    authors = User.objects.filter(
        following__user=user).prefetch_related(
        "recipes").order_by("-username")
    paginator = Paginator(authors, PAGES_SUBSCRIBE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(
        request,
        "recipes/subscription.html",
        {"page": page,
         "paginator": paginator}
    )


@login_required
def purchase(request):
    """Return purchases."""
    user = request.user
    purchases = Purchase.objects.filter(user=user).prefetch_related("recipe")
    return render(
        request,
        "recipes/shopList.html",
        {"purchases": purchases}
    )
