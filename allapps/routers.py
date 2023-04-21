from rest_framework_nested import routers

from allapps.auth.viewsets import LoginViewSet, RefreshViewSet, RegisterViewSet
from allapps.comment.viewsets import CommentViewSet
from allapps.offer.viewsets import OfferViewSet
from allapps.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# Auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# User
router.register(r'user', UserViewSet, basename='user')

# Offer
router.register(r'offer', OfferViewSet, basename='offer')

offers_router = routers.NestedSimpleRouter(router, r'offer', lookup='offer')
offers_router.register(r'comment', CommentViewSet, basename='offer-comment')

urlpatterns = [
    *router.urls,
    *offers_router.urls,
]
