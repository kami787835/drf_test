from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Category, Product, Order


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для профиля пользователя."""
    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории товаров."""

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для товаров."""
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='categories', many=True, write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'category_ids', 'price']


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для заказов."""
    user = serializers.StringRelatedField()
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'product_id', 'quantity']
