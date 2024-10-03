import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

from rest_framework.test import APIClient

from cats.models import Breed, Kitty

pytestmark = pytest.mark.django_db


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'tests/test_example_db_data.json')


@pytest.fixture
def user(db):
    return User.objects.first()


@pytest.fixture
def breed(db):
    return Breed.objects.create(name='MainKun')


@pytest.fixture
def kitty(db, breed, user):
    return Kitty.objects.create(
        color='White',
        age_in_months=36,
        description='White kitty',
        breed=breed,
        owner=user
    )


@pytest.fixture
def auth_client(user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def no_auth_client():
    api_client = APIClient()
    return api_client
