from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import BlogSerializer
from .models import Blog


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().order_by('published')
    serializer_class = BlogSerializer
    pagination_class = StandardResultsSetPagination
    filter_fields = BlogSerializer.filter_fields
