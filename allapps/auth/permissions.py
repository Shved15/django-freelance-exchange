from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    """Permissions for the User model."""
    def has_object_permission(self, request, view, obj):
        """Determines if the user has the right to access the object."""
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ["offer"]:
            return bool(request.user and request.user.is_authenticated)

        return False

    def has_permission(self, request, view):
        """Determines whether the user has the right to access the list of objects."""
        if view.basename in ["offer"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS

            return bool(request.user and request.user.is_authenticated)

        return False
