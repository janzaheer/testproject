from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField(max_length=200)
    date = serializers.DateTimeField()
