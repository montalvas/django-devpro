from django.urls import reverse
from task.models import Task
import pytest


@pytest.fixture
def response(client, db):
    resp = client.post(reverse('task:home'), data={'name': 'Task'})
    return resp
    # Simula uma post response com os dados

def test_task_exist_in_database(response):
    assert Task.objects.exists()
    # Verificando se está registrado no banco de dados

def test_task_redirect(response):
    assert response.status_code == 302
    # Verificando se foi redirecionado após salvar os dados

@pytest.fixture
def response_invalid(client, db):
    resp = client.post(reverse('task:home'), data={'name': ''})
    return resp
    # Simula uma post response sem os dados

def test_task_not_exist_in_database(response_invalid):
    assert not Task.objects.exists()
    # Verificando se a tarefa não está registrada

def test_task_redirect_invalid(response_invalid):
    assert response_invalid.status_code == 400
    # Verificando se foi não houve redirecionamento