from django.contrib.auth.models import User
from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    article_title = serializers.CharField(source="title", min_length=10)
    id = serializers.IntegerField(read_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'is_active')


class DetailedArticleSerializer(ArticleSerializer):
    content = serializers.CharField()
    author_name = serializers.CharField(source='author.username')



class YouTubeSnippetSerializer(serializers.Serializer):
    video_title = serializers.CharField(source='title')

class YouTubeSerializer(serializers.Serializer):
    my_etag = serializers.CharField(source='etag')
    # my_snippet = YouTubeSnippetSerializer(source='snippet')
    my_title = serializers.CharField(source='snippet.title')