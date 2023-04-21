from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from allapps.abstract.viewsets import AbstractViewSet
from allapps.auth.permissions import UserPermission
from allapps.offer.models import Offer
from allapps.offer.serializers import OfferSerializer


class OfferViewSet(AbstractViewSet):
    """ViewSet for the Offer model. Allows you to perform CRUD operations on Offer objects."""
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = OfferSerializer
    filterset_fields = ["author__public_id"]

    def get_queryset(self):
        """Returns a QuerySet of all Offer objects."""
        return Offer.objects.all()

    def get_object(self):
        """Returns an Offer object with the given public_id."""
        obj = Offer.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        """Creates a new Offer object. ValidationError: If invalid data is entered."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # The “like” method is called when a POST request is sent to an address containing “pk”.
    # This method adds a like from the current user to the specified instance of “Offer”.
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        # Method will automatically return the concerned post using the ID passed to the URL request.
        offer = self.get_object()
        user = self.request.user

        user.like_offer(offer)

        serializer = self.serializer_class(offer, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    # Removes the like from the current user for the specified “Offer” instance.
    @action(methods=['post'], detail=True)
    def remove_like(self, request, *args, **kwargs):
        offer = self.get_object()
        user = self.request.user

        user.remove_like_offer(offer)

        serializer = self.serializer_class(offer, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
