from rest_framework import viewsets


class AbstractViewSet(viewsets.ModelViewSet):
    """An abstract ViewSet for models that have a creation and update date.
    Supports filtering and sorting by creation and update dates."""
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']
