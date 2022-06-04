from rest_framework import serializers
from rest_framework.validators import *
from .models import Article, Category
import re


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='cat.name')
    author_username = serializers.ReadOnlyField(source='author.username')
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    @classmethod
    def __url_validator(cls, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        try:
            is_url = re.findall(regex, url)[0]
            return True
        except IndexError:
            return False

    def validate(self, attrs):
        if not attrs['title'].isascii():
            raise serializers.ValidationError("Only ASCII symbols in title")
        if not self.__url_validator(attrs['photo']):
            raise serializers.ValidationError("Photo field must contain valid URL")
        attrs['is_published'] = False
        return attrs

    class Meta:
        model = Article
        fields = ('title', 'cat', 'category',
                  'url', 'slug', 'content', 'photo',
                  'time_create', 'time_update', 'is_published',
                  'author_username',
                  )
