import pytest

from allapps.fixtures.user import user
from allapps.fixtures.offer import offer
from allapps.comment.models import Comment


@pytest.mark.django_db
def test_create_comment(user, offer):
    comment = Comment.objects.create(author=user, offer=offer, body="Test Comment Body")
    assert comment.author == user
    assert comment.offer == offer
    assert comment.body == "Test Comment Body"
