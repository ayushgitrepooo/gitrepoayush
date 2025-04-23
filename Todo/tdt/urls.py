from django.urls import path

from .views import ListCreateItemAPIView, RetrieveUpdateDestroyItemAPIView



urlpatterns = [
    path('tdt/', ListCreateItemAPIView.as_view(), name='list-create'),
    path('tdt/<pk>/', RetrieveUpdateDestroyItemAPIView.as_view(), name='list-create'),
    
]
