from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import viewsets
from .models import Category, Product, Order, OrderItem

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    
class OrderViewSet(viewsets.ModelViewSet):
     queryset = Order.objects.all()
     serializer_class = OrderSerializer        