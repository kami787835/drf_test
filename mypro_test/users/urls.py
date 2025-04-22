from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, CategoryViewSet, ProductViewSet, OrderViewSet

# Создаем роутер и регистрируем ViewSet'ы
router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='userprofile')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),  # Подключаем маршруты API
]
