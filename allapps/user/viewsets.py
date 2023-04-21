from rest_framework.permissions import IsAuthenticated

from allapps.abstract.viewsets import AbstractViewSet
from allapps.auth.permissions import UserPermission
from allapps.user.models import User
from allapps.user.serializers import UserSerializer


class UserViewSet(AbstractViewSet):
    """A ViewSet for listing or retrieving users."""
    http_method_names = ('patch', 'get')
    permission_classes = (IsAuthenticated, UserPermission)
    serializer_class = UserSerializer

    def get_queryset(self):
        """Get the queryset for this view set based on the request."""
        if self.request.user.is_superuser:
            return User.objects.all()
        # If the user is not a superuser, exclude a superusers from the queryset.
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        """Get the object to be used by this view set based on the request."""
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
