import pytest

from allapps.fixtures.user import user
from allapps.fixtures.offer import offer

from allapps.comment.models import Comment


@pytest.fixture
def comment(db, user, offer):
    return Comment.objects.create(author=user, offer=offer, body="Test Comment Body")
