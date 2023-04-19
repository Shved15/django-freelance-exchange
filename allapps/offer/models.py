from django.db import models

from allapps.abstract.models import AbstractManager, AbstractModel


class OfferManager(AbstractManager):
    """Offer model manager."""
    pass


class Offer(AbstractModel):
    """Offer model."""
    author = models.ForeignKey(to="allapps_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = OfferManager()

    def __str__(self):
        return f"{self.author.name}"
