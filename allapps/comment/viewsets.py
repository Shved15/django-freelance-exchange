from django.http.response import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from allapps.abstract.viewsets import AbstractViewSet
from allapps.auth.permissions import UserPermission
from allapps.comment.models import Comment
from allapps.comment.serializers import CommentSerializer


class CommentViewSet(AbstractViewSet):
    """ViewSet for the Comment model."""
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        """If the user is a superuser, he gets all the comments. If the user is not
         superuser, then only the comments associated with the specified offer_pk are returned."""
        if self.request.user.is_superuser:
            return Comment.objects.all()

        offer_pk = self.kwargs['offer_pk']
        if offer_pk is None:
            return Http404
        queryset = Comment.objects.filter(offer__public_id=offer_pk)

        return queryset

    def get_object(self):
        """Gets the Comment instance by its public_id."""
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj

    def create(self, request, *args, **kwargs):
        """Creates a new Comment instance."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["post"], detail=True)
    def like(self, request, *args, **kwargs):
        comment = self.get_object()
        user = self.request.user

        user.like_comment(comment)

        serializer = self.serializer_class(comment)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def remove_like(self, request, *args, **kwargs):
        comment = self.get_object()
        user = self.request.user

        user.remove_like_comment(comment)

        serializer = self.serializer_class(comment)

        return Response(serializer.data, status=status.HTTP_200_OK)

