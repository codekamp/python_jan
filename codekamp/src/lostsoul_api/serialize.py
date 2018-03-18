from django.contrib.auth.models import User
from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    article_title = serializers.CharField(source="title", min_length=10)
    id = serializers.IntegerField(read_only=True)

class DetailedArticleSerializer(ArticleSerializer):
    content = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'is_active')