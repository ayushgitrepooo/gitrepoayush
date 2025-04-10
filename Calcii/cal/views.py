from rest_framework import viewsets
from .models import Calculator
from .serializers import CalculatorSerializer

# Create your views here.

class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer