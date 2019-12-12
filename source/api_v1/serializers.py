from rest_framework import serializers
from webapp.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)
    rating = serializers.CharField(read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'text', 'created_at', 'status', 'author_name', 'author_email', 'rating')


class QuoteUpdateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    author_name = serializers.CharField(read_only=True)
    author_email = serializers.EmailField(read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'text', 'created_at', 'status', 'author_name', 'author_email', 'rating')


class QuoteRatingSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    author_name = serializers.CharField(read_only=True)
    author_email = serializers.EmailField(read_only=True)
    status = serializers.CharField(read_only=True)
    text = serializers.CharField(read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'text', 'created_at', 'status', 'author_name', 'author_email', 'rating')