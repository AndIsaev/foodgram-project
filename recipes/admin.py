from django.contrib import admin
from .models import (Recipe, Tag,
                     Ingredient, Quantity,
                     Purchase, Favorite,
                     Follow)


class QuantityInstanceInline(admin.TabularInline):
    model = Quantity


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "pub_date")
    search_fields = ("title",)
    list_filter = ("pub_date",)
    inlines = [QuantityInstanceInline, ]
    empty_value_display = "-пусто-"


class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "display_name", "color")


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("title", "dimension")
    search_fields = ("title",)


class QuantityAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    search_fields = ('recipe',)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ('user',)


admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quantity, QuantityAdmin)
