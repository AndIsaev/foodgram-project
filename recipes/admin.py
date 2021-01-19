from django.contrib import admin
from .models import Recipe, Tag, Ingredient, Quantity


class QuantityInstanceInline(admin.TabularInline):
    model = Quantity

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "pub_date")
    search_fields = ("title", )
    list_filter = ("pub_date",)
    inlines = [QuantityInstanceInline, ]
    empty_value_display = "-пусто-"


admin.site.register(Recipe, RecipeAdmin)
