from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from pip._internal.req.req_file import get_file_content
from recipes.models import Purchase, Quantity
from django.http import HttpResponse


def get_file_content(ingredients, user):
    filename = ('Shopping list from '
                f'{datetime.now().strftime("%d.%m.%y %H.%M.%S")}.txt')
    file_content = ''
    for ingredient in ingredients:
        ingredient_title = ingredient[
            'ingredient__title'][0].upper() + ingredient[
                'ingredient__title'][1:]
        ingredient_dimension = ingredient['ingredient__dimension']
        amount_sum = ingredient['amount__sum']

        file_content += (f'{ingredient_title} '
                         f'({ingredient_dimension}) — {amount_sum}  ;' + '\n')
    return filename, file_content


@login_required
def get_purchase_txt(request):
    user = request.user
    purchases_id = Purchase.objects.filter(user=user).values_list('recipe')
    ingredients = Quantity.objects.filter(
        recipe__in=purchases_id).prefetch_related('ingredient').values(
        'ingredient__title', 'ingredient__dimension').annotate(Sum('amount'))
    filename, file_content = get_file_content(ingredients, user)
    response = HttpResponse(file_content,
                            content_type='application/text charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
