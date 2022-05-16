from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'content', 'photo', 'time_create', 'time_update', 'is_published',)
