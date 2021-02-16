from django import template

from recipes.models import Follow, Purchase, Favorite

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='check_following')
def check_following(author, user):
    result = Follow.objects.filter(author=author.id, user=user.id).exists()
    return result


@register.filter(name='count_recipe')
def count_recipe(count):
    tmp = str(count - 3)
    if tmp[-1] == 1:
        return '1 рецепт'
    elif tmp[-1] in [2, 3, 4]:
        return f'{tmp} рецепта'
    return f'{tmp} рецептов'


@register.filter(name='check_purchase')
def check_purchase(user, recipe):
    result = Purchase.objects.filter(user=user, recipe=recipe).exists()
    return result


@register.filter(name='check_favorites')
def check_favorites(user, recipe):
    result = Favorite.objects.filter(user=user, recipe=recipe).exists()
    return result

@register.filter(name='get_count_purchase')
def get_count_purchase(user):
    result = Purchase.objects.filter(user=user).count()
    return result

