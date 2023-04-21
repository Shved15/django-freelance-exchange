from rest_framework import serializers
from django.conf import settings

from allapps.abstract.serializers import AbstractSerializer
from allapps.user.models import User


class UserSerializer(AbstractSerializer):
    """The UserSerializer class serializes objects of the User class."""
    offers_count = serializers.SerializerMethodField()

    def get_offers_count(self, instance):
        return instance.offer_set.all().count()

    def to_representation(self, instance):
        """The to_representation method overrides the base class method, adding logic to display the avatar."""
        # If the avatar is not set, sets it to the default value.
        # If debug mode is enabled, changes the avatar URL to an absolute URL.
        representation = super().to_representation(instance)
        if not representation["avatar"]:
            representation["avatar"] = settings.DEFAULT_AVATAR_URL
            return representation
        if settings.DEBUG:  # debug enabled for dev
            request = self.context.get("request")
            representation["avatar"] = request.build_absolute_uri(
                representation["avatar"]
            )
        return representation

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = ["id", "username", "name", "first_name", "last_name", "bio",
                  "avatar", "email", "is_active", "created", "updated", "offers_count"]
        # List of all the fields that can only be read by the user
        read_only_field = ["is_active"]
