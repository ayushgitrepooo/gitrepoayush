from django.contrib import admin
from .models import BlogCategory, BlogPost, Like, Comment, Userpfp

# Register your models here.

@admin.register(BlogPost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    list_filter = ['title']
    search_fields = ['title', 'created_at']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [ 'post', 'liked_at']
    search_fields = [ 'created_at']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'created_at']
    search_fields = ['content', 'created_at']    
     

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Userpfp)
class UserpfpAdmin(admin.ModelAdmin):
    list_display = ['user']
       
        