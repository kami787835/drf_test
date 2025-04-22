from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """Профиль пользователя (один к одному с User)."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile',
        verbose_name="Пользователь"
    )
    bio = models.TextField(blank=True, verbose_name="О себе")

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"


class Category(models.Model):
    """Категория товаров."""
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар (много ко многим с категориями)."""
    name = models.CharField(max_length=255, verbose_name="Название товара")
    categories = models.ManyToManyField(
        Category, related_name='products', verbose_name="Категории"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Order(models.Model):
    """Заказ (один ко многим: один пользователь может делать много заказов)."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders',
        verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
