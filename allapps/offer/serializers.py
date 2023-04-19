from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from allapps.abstract.serializers import AbstractSerializer
from allapps.offer.models import Offer
from allapps.user.models import User
from allapps.user.serializers import UserSerializer


class OfferSerializer(AbstractSerializer):
    """The serializer for the Offer model."""
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        """Checks that the offer author is the current user."""
        if self.context["request"].user != value:
            raise ValidationError("You can't create a offer for another user.")
        return value

    def update(self, instance, validated_data):
        # Check if the instance object has been previously edited.
        # If not, then add the edited key to validated data with the value True.
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        """Converts the Offer object to a dictionary that can be serialized to JSON."""
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data

    class Meta:
        model = Offer
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ["edited"]
