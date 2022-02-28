from django.urls import reverse
from task.models import Task
from pytest_django.asserts import assertContains
import pytest


@pytest.fixture
def pending_task(db):
    return Task.objects.create(name='Task 1', done=False)


@pytest.fixture
def response_pending_task(client, pending_task):
    resp = client.post(
        reverse('task:update', kwargs={'task_id': pending_task.id}),
        data={'done':'true', 'name': f'{pending_task.name}-edited'}
    )
    return resp

def test_status_code(response_pending_task):
    assert response_pending_task.status_code == 302

def test_task_done(response_pending_task):
    assert Task.objects.first().done

@pytest.fixture
def done_task(db):
    return Task.objects.create(name='Task 1', done=True)


@pytest.fixture
def response_done_task(client, done_task):
    resp = client.post(
        reverse('task:update', kwargs={'task_id': done_task.id}),
        data={'name': f'{done_task.name}-edited'}
    )
    return resp

def test_task_done(response_done_task):
    assert not Task.objects.first().done