from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Recipe


def index(request):
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "singlePageNotAuth.html",
        {"page": page,
         "paginator": paginator,}
    )
