from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    ISBN = serializers.CharField(max_length=10)
    Title = serializers.CharField(max_length=200)
    Author = serializers.CharField(max_length=200)
    Date = serializers.DateTimeField()

    def create(self, validated_data):
        return Book.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.ISBN = validated_data.get('ISBN', instance.ISBN)
        instance.Title = validated_data.get('Title', instance.Title)
        instance.Author = validated_data.get('Author', instance.Author)
        instance.Date = validated_data.get('Date', instance.Date)
        instance.save()
        return instance
