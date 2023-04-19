from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from allapps.user.serializers import UserSerializer


# Inherit from the standard serializer to get an access token
class LoginSerializer(TokenObtainPairSerializer):

    # Call the data validation method of the parent class
    def validate(self, attrs):
        data = super().validate(attrs)

        # Get updated access token
        refresh = self.get_token(self.user)

        # Add: user data to the response, a string representation of the the refresh token and the access token
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # If set to True, update the user's last login time
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
