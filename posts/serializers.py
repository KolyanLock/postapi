from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'image', 'content', 'author', 'created_at', 'updated_at', 'views', 'category',
                  'tags']
        read_only_fields = ['created_at', 'author', 'updated_at', 'views']
