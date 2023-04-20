from rest_framework.permissions import SAFE_METHODS, BasePermission


class UserPermission(BasePermission):
    """Permissions for the User model."""
    def has_object_permission(self, request, view, obj):
        """Determines if the user has the right to access the object."""
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ["offer"]:
            return bool(request.user and request.user.is_authenticated)

        if view.basename in ["offer-comment"]:
            if request.method in ['DELETE']:
                return bool(request.user.is_superuser or request.user in [obj.author, obj.offer.author])

            return bool(request.user and request.user.is_authenticated)

        return False

    def has_permission(self, request, view):
        """Determines whether the user has the right to access the list of objects."""
        if view.basename in ["offer", "offer-comment"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS

            return bool(request.user and request.user.is_authenticated)

        return False
