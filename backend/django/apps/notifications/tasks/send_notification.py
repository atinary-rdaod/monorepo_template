"""Celery task that simulates sending a notification.

Pattern: thin async wrapper around any side-effecting operation. The HTTP
request returns immediately with the row in `PENDING`; the worker flips
the status to `SENT` (or `FAILED`) once it's done. The client polls
`GET /api/notifications/` for updates.

Swap `time.sleep` + the log line for a real provider (SES, Sendgrid, ...).
"""

import time

from celery import shared_task
from django.utils import timezone

from apps.notifications.models import NotificationModel
from util import get_logger

LOGGER = get_logger(__name__)


@shared_task(name="notifications.send")
def send_notification(notification_id: str) -> None:
    notification = NotificationModel.objects.get(id=notification_id)
    try:
        # Pretend we're talking to an email provider.
        time.sleep(2)
        LOGGER.info(
            "notification sent",
            id=notification_id,
            recipient=notification.recipient,
            subject=notification.subject,
        )
        notification.status = NotificationModel.STATUS_SENT
        notification.sent_at = timezone.now()
        notification.save(update_fields=["status", "sent_at", "updated_at"])
    except Exception as exc:
        notification.status = NotificationModel.STATUS_FAILED
        notification.error = str(exc)
        notification.save(update_fields=["status", "error", "updated_at"])
        raise
