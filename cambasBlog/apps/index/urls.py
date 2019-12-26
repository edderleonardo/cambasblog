from django.urls import path
from .views import Index, Posts, DetailPost

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('posts/', Posts.as_view(), name='posts'),
    path('post/detail/<int:pk>/', DetailPost.as_view(), name='detail-posts'),
]
