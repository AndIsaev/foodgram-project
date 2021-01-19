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


class TagAdmin(admin.ModelAdmin):
    list_display = ("key", "value")


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("title", "dimension")
    search_fields = ("title",)


class QuantityAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    search_fields = ('recipe',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quantity, QuantityAdmin)
