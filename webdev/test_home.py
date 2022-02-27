from django.test import Client


def test_status_home_code(client:Client):
    response = client.get('/')
    assert response.status_code == 200