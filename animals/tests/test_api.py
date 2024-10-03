import pytest
from rest_framework import status

from cats.models import Breed, Kitty

pytestmark = pytest.mark.django_db


class TestAPIAuth:
    def test_get_breeds(self, auth_client):
        response = auth_client.get(path='/api/v1/breeds/')
        assert response.status_code == status.HTTP_200_OK

    def test_create_kitty(self, user, auth_client):
        breed = Breed.objects.first()
        data = {
            "color": "Зелёная",
            "age_in_months": 25,
            "description": "Рыжая кошка",
            'breed': breed.id
        }
        response = auth_client.post(path='/api/v1/kitten/',
                                    data=data,
                                    format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_kitten(self, auth_client):
        response = auth_client.get(path='/api/v1/kitten/')
        assert response.status_code == status.HTTP_200_OK

    def test_get_kitten_by_filter(self, auth_client):
        breed = Breed.objects.first()
        response = auth_client.get(path=f'/api/v1/kitten/?breed={breed.name}')
        assert response.status_code == status.HTTP_200_OK

    def test_get_kitty(self, auth_client):
        kitty = Kitty.objects.first()
        response = auth_client.get(path=f'/api/v1/kitten/{kitty.id}/')
        assert response.status_code == status.HTTP_200_OK

    def test_update_kitty(self, auth_client, kitty):
        data = {
            "name": "New name",
            "color": "Зелёная",
            "age_in_months": 26,
            "description": "Рыжая кошка",
            'breed': 1,
        }
        response = auth_client.put(path=f'/api/v1/kitten/{kitty.id}/',
                                   data=data,
                                   format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_patch_kitty(self, kitty, auth_client):
        data = {
            "color": "Красная",
        }

        response = auth_client.patch(path=f'/api/v1/kitten/{kitty.id}/',
                                     data=data,
                                     format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_delete_kitty(self, kitty, auth_client):
        response = auth_client.delete(path=f'/api/v1/kitten/{kitty.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_get_ratings(self, auth_client):
        kitty = Kitty.objects.first()
        response = auth_client.get(path=f'/api/v1/ratings/')
        assert response.status_code == status.HTTP_200_OK

    def test_create_rating(self, auth_client, user):
        kitty = Kitty.objects.exclude(owner=user).first()
        data = {
            "rating": 5,
            "kitty": kitty.id
        }
        response = auth_client.post(path=f'/api/v1/ratings/',
                                    data=data,
                                    format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_patch_rating(self, auth_client, user):
        kitty = Kitty.objects.exclude(owner=user).first()
        kitty_rating_first = kitty.ratings.filter(owner=user).first()
        data = {
            "rating": 3,
        }
        response = auth_client.patch(path=f'/api/v1/ratings/{kitty_rating_first.id}/',
                                     data=data,
                                     format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_rating(self, auth_client, user):
        kitty = Kitty.objects.exclude(owner=user).first()
        kitty_rating_first = kitty.ratings.filter(owner=user).first()

        response = auth_client.delete(path=f'/api/v1/ratings/{kitty_rating_first.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestAPINotAuth:
    def test_get_breeds(self, no_auth_client):
        response = no_auth_client.get(path='/api/v1/breeds/')
        assert response.status_code == status.HTTP_200_OK

    def test_create_kitty(self, user, breed, no_auth_client):
        data = {
            "color": "Зелёная",
            "age_in_months": 25,
            "description": "Рыжая кошка",
            'breed': breed.id
        }
        response = no_auth_client.post(path='/api/v1/kitten/',
                                       data=data,
                                       format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_kitty(self, user, breed, kitty, no_auth_client):
        data = {
            "color": "Зелёная",
            "age_in_months": 26,
            "description": "Рыжая кошка",
            'breed': breed.id,
        }
        response = no_auth_client.put(path=f'/api/v1/kitten/{kitty.id}/',
                                      data=data,
                                      format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_patch_kitty(self, user, breed, kitty, no_auth_client):
        data = {
            "color": "Красная",
        }

        response = no_auth_client.patch(path=f'/api/v1/kitten/{kitty.id}/',
                                        data=data,
                                        format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_kitty(self, kitty, no_auth_client):
        response = no_auth_client.delete(path=f'/api/v1/kitten/{kitty.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_ratings(self, no_auth_client):
        kitty = Kitty.objects.first()
        response = no_auth_client.get(path=f'/api/v1/ratings/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_rating(self, no_auth_client, user):
        kitty = Kitty.objects.exclude(owner=user).first()
        data = {
            "rating": 5,
            "kitty": kitty.id
        }
        response = no_auth_client.post(path=f'/api/v1/ratings/',
                                       data=data,
                                       format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_patch_rating(self, no_auth_client, user):
        kitty = Kitty.objects.exclude(owner=user).first()
        kitty_rating_first = kitty.ratings.filter(owner=user).first()
        data = {
            "rating": 3,
        }
        response = no_auth_client.patch(path=f'/api/v1/ratings/{kitty_rating_first.id}/',
                                        data=data,
                                        format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_rating(self, no_auth_client, user):
        kitty = Kitty.objects.exclude(owner=user).first()
        kitty_rating_first = kitty.ratings.filter(owner=user).first()

        response = no_auth_client.delete(path=f'/api/v1/ratings/{kitty_rating_first.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
