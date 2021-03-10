from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from recipes.models import Quantity, Recipe


@login_required
def get_purchase_txt(request):
    user = request.user
    recipes = Recipe.objects.filter(purchases__user=user)
    ingredients = {}
    ingredients_filter = Quantity.objects.filter(recipe__id__in=recipes)
    for ingredient in ingredients_filter:
        if ingredient in ingredients:
            ingredients[ingredient.ingredient] += ingredient.amount
        else:
            ingredients[ingredient.ingredient] = ingredient.amount
    ingredients_response = []
    for i, j in ingredients.items():
        ingredients_response.append(f"{i.title} ({i.dimension}) - {j}; \n")
    response = HttpResponse(ingredients_response, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="ingrediens.txt"'
    return response
