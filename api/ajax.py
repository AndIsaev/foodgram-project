import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from recipes.models import Ingredient, Favorite, Recipe, User, Follow


def found_ingredient(request):
    query = request.GET.get("query").lower()[:-1]
    ingredients = Ingredient.objects.filter(
        title__icontains=query).values("title", "dimension").order_by("title")
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


@login_required
@csrf_exempt
def add_subscription(request):
    body = json.loads(request.body)
    author = get_object_or_404(User, id=int(body['id']))
    user = get_object_or_404(User, id=request.user.id)

    if user.id != author.id:
        Follow.objects.get_or_create(user=user, author=author)
        return JsonResponse({"success": True})
    response = HttpResponse()
    response.status_code = 400
    return response


@login_required
@csrf_exempt
def remove_subscription(request, author_id):
    author = get_object_or_404(User, id=author_id)
    user = get_object_or_404(User, id=request.user.id)
    Follow.objects.filter(user=user, author=author).delete()
    return JsonResponse({"success": True})
