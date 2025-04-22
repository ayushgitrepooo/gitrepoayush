from rest_framework import viewsets
from .models import BlogCategory, BlogPost, Userpfp, Like, Comment
from .serializers import BlogCategorySerializer, BlogPostSerializer, LikeSerializer, CommentSerializer, UserpfpSerializer

# Create your views here.


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    
class UserpfpViewSet(viewsets.ModelViewSet):
    queryset = Userpfp.objects.all()
    serializer_class = UserpfpSerializer         
        