from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializer import CategotySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategotySerializer
    queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
