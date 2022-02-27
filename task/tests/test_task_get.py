from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest


@pytest.fixture
def response(client):
    resp = client.get(reverse('task:home'))
    return resp

def test_status_code(response):
    assert response.status_code == 200
    # Verifica se a pagina carregou sem erros

def test_form_present(response):
    assertContains(response, '<form')
    # Verifica se recebeu o <form>

def test_form_button_submit(response):
    assertContains(response, '<button type="submit"')
    # Verifica se possui o botao de salvar
