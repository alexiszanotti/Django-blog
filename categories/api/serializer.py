from rest_framework import serializers
from categories.models import Category


class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'published']
