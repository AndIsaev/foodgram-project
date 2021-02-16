import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from recipes.models import Ingredient, Favorite, Recipe




def found_ingredient(request):
    query = request.GET.get("query").lower()[:-1]
    ingredients = Ingredient.objects.filter(
        title__icontains=query).values("title", "dimension").order_by('title')
    return JsonResponse(list(ingredients), safe=False)


@login_required
@csrf_exempt
def add_favorites(request):
    body = json.loads(request.body)
    recipe = get_object_or_404(Recipe, id=int(body['id']))
    user = request.user

    Favorite.objects.get_or_create(user=user, recipe=recipe)

    return JsonResponse({"success": True})


@login_required
@csrf_exempt
def remove_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    user = request.user

    Favorite.objects.filter(user=user, recipe=recipe).delete()

    return JsonResponse({"success": True})