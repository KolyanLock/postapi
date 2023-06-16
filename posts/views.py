from rest_framework import viewsets

from .filters import PostFilter
from .models import Post
from .permissions import IsAuthorOrAdminOrReadOnly
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    permission_classes = [IsAuthorOrAdminOrReadOnly]

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
