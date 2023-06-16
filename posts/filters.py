from django_filters import rest_framework as filters

from .models import Post


class PostFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__username')
    category = filters.CharFilter(field_name='category__slug')
    tags = filters.CharFilter(field_name='tags__slug')

    class Meta:
        model = Post
        fields = ['author', 'category', 'tags']
