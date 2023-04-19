from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from allapps.abstract.viewsets import AbstractViewSet
from allapps.offer.models import Offer
from allapps.offer.serializers import OfferSerializer


class OfferViewSet(AbstractViewSet):
    """ViewSet for the Offer model. Allows you to perform CRUD operations on Offer objects."""
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = OfferSerializer

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
