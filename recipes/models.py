from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint, Q, CheckConstraint
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    """Model tags."""
    title = models.CharField('Имя тега', max_length=60, db_index=True)
    display_name = models.CharField('Имя тега для шаблона', max_length=60)
    color = models.CharField('Цвет тега', max_length=15)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """Model recipes."""
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
    tags = models.ManyToManyField(Tag, verbose_name='Тег',
                                  related_name='recipes')
    time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления'
    )
    pub_date = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name="Дата публикации"
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    """Model ingredients."""
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    dimension = models.CharField(max_length=100, verbose_name='Мера')

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return f"{self.title} ({self.dimension})"


class Quantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    amount = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Количество'


class Follow(models.Model):
    """Model for subscribe."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ('author',)
        constraints = [
            UniqueConstraint(
            fields=["user", "author"],
            name='unique_follow')]


class Purchase(models.Model):
    """Model our purchase."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='purchases',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='purchases',
                               verbose_name='Рецепт')

    class Meta:
        verbose_name = 'Покупки'


class Favorite(models.Model):
    """Model favorites recipes."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorites',
                               verbose_name='Понравившейся рецепт')

    class Meta:
        verbose_name = 'Избранное'
        constraints = [
            UniqueConstraint(
                fields=["user", "recipe"],
                name='unique_favorite')]
