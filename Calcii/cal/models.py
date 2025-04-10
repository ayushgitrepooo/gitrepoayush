from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Calculator(models.Model):
    OPERATIONS_CHOICE = [
        ('add', 'Addition'),
        ('subtract', 'Subtraction'),
        ('multiply', 'Multiplication'),
        ('divide', 'Division')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num1 = models.FloatField()
    num2 = models.FloatField()
    operations = models.CharField(max_length=10, choices=OPERATIONS_CHOICE)
    result = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    
    
    def __str__(self):
        return f"{self.num1} {self.operations} {self.num2} {self.result}"
  
    