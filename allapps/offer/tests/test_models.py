import pytest

from allapps.fixtures.user import user
from allapps.offer.models import Offer


@pytest.mark.django_db
def test_create_post(user):
    offer = Offer.objects.create(author=user, body="Test Offer Body")
    assert offer.body == "Test Offer Body"
    assert offer.author == user
