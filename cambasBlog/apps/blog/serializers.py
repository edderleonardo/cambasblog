from rest_framework import serializers
from .models import Blog
from ..users.serializers import AuthorSerializer


class BlogSerializer(serializers.ModelSerializer):
    filter_fields = ('author', 'author__country')
    author = AuthorSerializer()

    class Meta:
        model = Blog
        fields = [
            'pk',
            'published',
            'title',
            'content',
            'author',
        ]