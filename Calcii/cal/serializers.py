from .models import Calculator, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'date_joined', 'is_active', 'email']
        

class CalculatorSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only = True)
    class Meta:
        model = Calculator
        fields = '__all__'
        read_only_fields = ['result', 'created_at']

           
    def validate(self, data):
        if data ['operations'] == 'divide' and data['num2'] == 0:
            raise serializers.ValidationError("Division by zero is not allowed.")
        return data
    
    def create(self, validated_data):
        num1 = validated_data['num1']
        num2 = validated_data['num2']
        operations = validated_data['operations']
        
        
        if operations == 'add':
            validated_data['result'] = num1 + num2
        elif operations == 'subtract':
            validated_data['result'] = num1 - num2
        elif operations == 'multiply':
            validated_data['result'] = num1 * num2
        elif operations == 'divide':
            validated_data['result'] = num1 / num2
                    
        return super(). create(validated_data)            
                    


                

