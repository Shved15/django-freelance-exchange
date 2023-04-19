from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from allapps.abstract.models import AbstractManager, AbstractModel


# UserManager model, so we can have methods to create a user and a superuser
class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    """A custom user model that implements the required fields for authentication."""
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)

    offers_liked = models.ManyToManyField(
        "allapps_offer.Offer",
        related_name="liked_by"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        # Returns the user's full name, concatenates the first_name and last_name fields
        return f"{self.first_name} {self.last_name}"

    def like(self, offer):
        """Like `offer` if it hasn't been done yet."""
        return self.offers_liked.add(offer)

    def remove_like(self, offer):
        """Remove a like from a `offer`"""
        return self.offers_liked.remove(offer)

    def has_liked(self, offer):
        """Return True if the user has liked a `offer`; else False."""
        return self.offers_liked.filter(pk=offer.pk).exists()
