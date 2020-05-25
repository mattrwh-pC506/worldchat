import pytest
import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def fake_password():
    return faker.password()


@pytest.fixture
def user_factory(db):
    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = User
        
        id = 1
        email = faker.email()
        username = faker.user_name()

    return UserFactory


@pytest.fixture
def sample_user(user_factory, fake_password):
    user = user_factory()
    user.set_password(fake_password)
    user.save()
    return user
