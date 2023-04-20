from django.db import models

from allapps.abstract.models import AbstractManager, AbstractModel


class CommentManager(AbstractManager):
    """Comment model manager"""
    pass


class Comment(AbstractModel):
    """We define the Comment model, which is a subclass of the AbstractModel class."""
    offer = models.ForeignKey("allapps_offer.Offer", on_delete=models.CASCADE)
    author = models.ForeignKey("allapps_user.User", on_delete=models.CASCADE)

    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.author.name
