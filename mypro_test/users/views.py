from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import UserProfile, Category, Product, Order
from .serializers import UserProfileSerializer, CategorySerializer, ProductSerializer, OrderSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """CRUD для профилей пользователей."""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD для категорий товаров."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD для товаров."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """CRUD для заказов."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
