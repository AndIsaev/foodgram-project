from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Recipe, Tag

# def get_filters_recipes(request, *args, **kwargs):
#     filters = request.GET.getlist('filters')
#     if filters:
#         recipes = Recipe.objects.filter(
#             tags__key__in=filters).filter(**kwargs).distinct()
#     else:
#         recipes = Recipe.objects.filter(**kwargs).all()
#
#     return filters, recipes
#
#
# def index(request):
#     filters, recipes = get_filters_recipes(request)
#     tags = Tag.objects.all()
#     paginator = Paginator(recipes, 6)
#     page_number = request.GET.get('page')
#     page = paginator.get_page(page_number)
#
#     content = {'page': page,
#                'paginator': paginator,
#                'tags': tags,
#                'filter': filters,
#                }
#
#     return render(request, 'index.html', content)


def index(request):
    """Возвращает до 11 последних записей."""
    return render(request, "index.html", {
        "recipes": list(
            Recipe
                .objects
                .all()
                .select_related("author")
                .values("author", "pub_date",
                         'image', 'ingredients', 'tags', 'time', 'description')[:6]
        )
    })

# def index(request):
#     latest = Recipe.objects.order_by("-pub_date")[:11]
#     return render(request, "index.html", {"posts": latest})