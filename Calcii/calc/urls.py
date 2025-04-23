from .views import CalculatorViewSet
from rest_framework .routers import DefaultRouter
from django.urls import path , include

router = DefaultRouter()
router.register (r'Calculator', CalculatorViewSet, basename = 'calc')


urlpatterns = [
    path('', include(router.urls)),
]

    

