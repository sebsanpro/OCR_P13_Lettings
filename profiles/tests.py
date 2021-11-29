import pytest

from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_url():
    User.objects.create(username='test',
                        password='azerty1234!',
                        last_name='nom de famille',
                        email="test@test.com")
    Profile.objects.create(user_id='1',
                           favorite_city='Paris')
    path = reverse('profile', kwargs={'username': 'test'})

    assert path == "/profiles/test/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_profiles_view():
    client = Client()
    User.objects.create(username='test',
                        password='azerty1234!',
                        last_name='nom de famille',
                        email="test@test.com")
    Profile.objects.create(user_id='1',
                           favorite_city='Paris')
    path = reverse('profile', kwargs={'username': 'test'})
    response = client.get(path)
    content = response.content.decode()
    expected_content_last_name = "<p>Last name: nom de famille</p>"
    expected_content_email = "<p>Email: test@test.com</p>"

    assert expected_content_last_name in content
    assert expected_content_email in content
    assert response.status_code == 200
