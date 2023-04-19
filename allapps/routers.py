from rest_framework import routers

from allapps.auth.viewsets.register import RegisterViewSet
from allapps.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# Auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

# User
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]
