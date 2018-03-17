from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    article_title = serializers.CharField(source="title")
    id = serializers.IntegerField()

class DetailedArticleSerializer(ArticleSerializer):
    content = serializers.CharField()