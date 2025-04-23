from rest_framework import serializers
from .models import Calculator, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_active', 'date_joined', 'email']
        

class CalculatorSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source = 'user', read_only = True)
    class Meta:
        model = Calculator
        fields = '__all__'
        read_only_fields = ['created_at', 'result']
        
        
    def validate(self, data):
        if data ['operation'] == 'divide' and data['a'] == 0:
            raise serializers.ValidationError('Division by zero not allowed.') 
        return data
    
    def create(self, validate_data):
        a = validate_data['a']
        b = validate_data['b']
        operation = validate_data['operation']
        
        if operation == 'add':
            validate_data['result'] = a + b
        elif operation == 'subtract':
            validate_data['result'] = a - b 
        elif operation == 'multiply':
            validate_data['result'] = a * b
        elif operation == 'divide':
            validate_data['result'] = a / b
        elif operation == 'module':
            validate_data['result'] = a ** b
            
        
        return super(). create(validate_data)                    
        
           
                