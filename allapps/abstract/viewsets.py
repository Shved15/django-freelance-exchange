from rest_framework import filters, viewsets


class AbstractViewSet(viewsets.ModelViewSet):
    """An abstract ViewSet for models that have a creation and update date.
    Supports filtering and sorting by creation and update dates."""
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']
