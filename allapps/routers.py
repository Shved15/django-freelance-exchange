from rest_framework import routers

from allapps.auth.viewsets import LoginViewSet, RefreshViewSet, RegisterViewSet
from allapps.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# Auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# User
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]
