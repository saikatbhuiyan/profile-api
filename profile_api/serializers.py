from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField()
    is_single = serializers.BooleanField(default=False)