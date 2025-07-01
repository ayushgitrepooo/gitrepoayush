from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('orderItems', CategoryViewSet, basename='orderItem')
router.register('orders', CategoryViewSet, basename='order')


urlpatterns = [
    path("", include(router.urls)),
]


