import pytest
from apps.notifications.models import NotificationModel
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_notification_is_sent_synchronously_under_eager_celery() -> None:
    """`CELERY_TASK_ALWAYS_EAGER = True` in test settings makes the Celery
    task run inline, so by the time the POST returns the status is SENT."""
    client = APIClient()
    payload = {"recipient": "demo@example.com", "subject": "hello", "body": "hi there"}

    response = client.post("/api/notifications/", payload, format="json")
    assert response.status_code == 202, response.content

    notification = NotificationModel.objects.get()
    assert notification.recipient == "demo@example.com"
    assert notification.status == NotificationModel.STATUS_SENT
    assert notification.sent_at is not None


@pytest.mark.django_db
def test_list_notifications() -> None:
    NotificationModel.objects.create(recipient="a@b.c", subject="s", body="b")
    response = APIClient().get("/api/notifications/")
    assert response.status_code == 200
    assert len(response.json()) == 1
