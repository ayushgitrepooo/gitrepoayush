from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BlogCategoryViewSet, BlogPostViewSet, LikeViewSet, UserpfpViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'blogcategory', BlogCategoryViewSet, basename='blog')
router.register(r'blogcpost', BlogPostViewSet, basename='blogp')
router.register(r'like', LikeViewSet, basename='like')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'userpfp', UserpfpViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
]
