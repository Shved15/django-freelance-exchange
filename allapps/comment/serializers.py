from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from allapps.abstract.serializers import AbstractSerializer
from allapps.comment.models import Comment
from allapps.offer.models import Offer
from allapps.user.models import User
from allapps.user.serializers import UserSerializer


class CommentSerializer(AbstractSerializer):
    """The serializer for the Comment model."""
    # SlugRelatedField is used to convert objects to strings using the specified object attribute as value.
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    offer = serializers.SlugRelatedField(queryset=Offer.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        """Checks that the current user, and the author of the comment match."""
        if self.context["request"].user != value:
            # Raise a ValidationError if the author is not equal to the current user
            raise ValidationError("You can't create a offer for another user.")
        return value

    def validate_offer(self, value):
        # Checks if the current offer value is a field of an existing comment instance or a new value.
        # If the instance already exists, the current value of the offer field is returned,
        # otherwise the value passed to the function is returned.
        if self.instance:
            return self.instance.offer
        return value

    def update(self, instance, validated_data):
        # Updates the fields of an existing comment instance with the data passed to the function.
        if not instance.edited:
            validated_data['edited'] = True

        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        """We get a dictionary with the data of the Comment instance using the parent's to_representation method."""
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep

    class Meta:
        model = Comment
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'offer', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ["edited"]
