import pytest
from django.urls import reverse

from .models import Task


@pytest.mark.django_db
def test_task_starts_incomplete():
    task = Task.objects.create(title="Learn Django")
    assert task.completed is False


@pytest.mark.django_db
def test_task_list_page_loads(client):
    response = client.get(reverse("task-list"))
    assert response.status_code == 200
    assert "My Tasks" in response.content.decode()