from rest_framework import serializers
from .models import Comment, BlogCategory, BlogPost, Like, Userpfp, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'date_joined', 'is_active', 'email']
        

class CommentSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)   # showing the user info in comment
    class Meta:
        model = Comment
        fields = '__all__'
        
class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        
class UserpfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userpfp
        fields = '__all__'
        
        
                    
        
                
          



