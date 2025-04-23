from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Item
from .serializers import ItemSerializer

class ListCreateItemAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class RetrieveUpdateDestroyItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    