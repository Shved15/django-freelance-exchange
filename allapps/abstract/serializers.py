from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    """An abstract class for model serializers. Defines the basic serialization logic
     and some common fields for all models."""
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
