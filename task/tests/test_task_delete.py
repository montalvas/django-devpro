from django.urls import reverse
from task.models import Task
from pytest_django.asserts import assertContains
import pytest


@pytest.fixture
def task(db):
    return Task.objects.create(name='Task 1', done=True)


@pytest.fixture
def response(client, task):
    resp = client.post(
        reverse('task:delete', kwargs={'task_id': task.id})
    )
    return resp

def test_delete_task(response, db):
    assert not Task.objects.exists()