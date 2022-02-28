from django.urls import reverse
from task.models import Task
from pytest_django.asserts import assertContains
import pytest


@pytest.fixture
def response(client, db):
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

@pytest.fixture
def pending_task_list(db):
    tasks = [
        Task(name='Task 1', done=False),
        Task(name='Task 2', done=False),
    ]

    Task.objects.bulk_create(tasks)
    return tasks

@pytest.fixture
def response_task_list(client, pending_task_list):
    resp = client.get(reverse('task:home'))
    return resp

def test_pending_task_list_present(response_task_list, pending_task_list):
    for task in pending_task_list:
        assertContains(response_task_list, task.name)