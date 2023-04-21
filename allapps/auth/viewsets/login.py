from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from allapps.auth.serializers import LoginSerializer


class LoginViewSet(ViewSet):
    """ViewSet for user authorization."""
    # use LoginSerializer to serialize data, allow: access to any user and only the POST method.
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """Creates a new login session."""
        serializer = self.serializer_class(data=request.data, context={'request': request})

        # check the data for validity, raise an exception on error
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
