import pytest
import factory
from faker import Factory as FakerFactory
import random
from chat.models import Chatter

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def chatter_factory(db, sample_user):
    class ChatterFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Chatter
        user = sample_user
        user_id = sample_user.id
        geocode = faker.pystr()
        usertag = faker.pystr()
        address = faker.address()
        online = faker.boolean()
    return ChatterFactory


@pytest.fixture
def sample_chatter(chatter_factory):
    chatter = chatter_factory()
    chatter.save()
    return chatter
