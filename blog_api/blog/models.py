from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class BlogCategory(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=100)
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post')
        
class Userpfp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    
          
         
        
    
    

    
    
    
    