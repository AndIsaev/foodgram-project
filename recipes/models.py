from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField(max_length=60, verbose_name='Тег')

    def __str__(self):
        return self.tag


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор публикации')
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        null=True,verbose_name='Описание'
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='Quantity',
        through_fields = ('recipe', 'ingredient'),
        verbose_name='Ингредиенты'
    )
    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True,
        verbose_name="Картинка"
    )
    tags = models.ManyToManyField(Tag, verbose_name='Тег')
    time = models.PositiveIntegerField(verbose_name='Время приготовления')
    pub_date = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name="Дата публикации"
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    dimension = models.CharField(max_length=100, verbose_name='Мера')

    def __str__(self):
        return f"{self.title} ({self.dimension})"


class Quantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    amount = models.PositiveIntegerField(verbose_name='Количество')
