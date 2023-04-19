from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from allapps.auth.serializers.register import RegisterSerializer


class RegisterViewSet(ViewSet):
    """ViewSet for registering new users."""
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """Registers a new user.
        Accepts a request with user data and creates a new user in the database.
        Returns data about the created user and API access tokens."""
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        # Create a dictionary with API access tokens
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        # Return data about the created user and API access tokens
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)
