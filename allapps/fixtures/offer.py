import pytest

from allapps.fixtures.user import user
from allapps.offer.models import Offer


@pytest.fixture
def offer(db, user):
    return Offer.objects.create(author=user, body="Test Offer Body")
