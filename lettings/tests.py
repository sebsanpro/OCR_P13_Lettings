import pytest

from django.urls import reverse, resolve
from django.test import Client
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_url():
    Address.objects.create(number=12,
                           street='par ici',
                           city='Toulouse',
                           state='OC',
                           zip_code=31000,
                           country_iso_code='FR')
    Letting.objects.create(title='ceci est le titre',
                           address_id=1)
    path = reverse('letting', kwargs={'letting_id': 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_lettings_view():
    client = Client()
    Address.objects.create(number=12,
                           street='par ici',
                           city='Toulouse',
                           state='OC',
                           zip_code=31000,
                           country_iso_code='FR')
    Letting.objects.create(title='ceci est le titre',
                           address_id=1)
    path = reverse('letting', kwargs={'letting_id': 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content_letting = "<h1>ceci est le titre</h1>"
    expected_content_adress = "<p>Toulouse, OC 31000</p>"

    assert expected_content_letting in content
    assert expected_content_adress in content
    assert response.status_code == 200
