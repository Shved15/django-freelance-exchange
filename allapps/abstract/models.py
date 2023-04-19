from django.db import models
import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):
    """Custom manager for AbstractModel that provides a method to retrieve an instance by its public_id."""
    def get_object_by_public_id(self, public_id):
        # Returns an instance of the model with the given public_id.
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


# An abstracts base model that provides a public_id field and timestamps.
class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract = True
