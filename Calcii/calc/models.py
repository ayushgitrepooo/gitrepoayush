from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Calculator(models.Model):
    OPERATION_CHOICES = [
        ('add', 'addition'),
        ('subtract', 'subtraction'),
        ('multiply', 'Multiplication'),
        ('divide', 'Division'),
        ('module', 'Modules')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    a = models.FloatField()
    b = models.FloatField()
    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    result = models.FloatField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.a} {self.operation} {self.b} {self.result}"
    
    