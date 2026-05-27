from django.db import models

from apps.core.models import BaseModel


class NotificationModel(BaseModel):
    """A simulated outgoing notification (e.g. email).

    The status is flipped from PENDING to SENT (or FAILED) by the
    `notifications.send` Celery task — the row is the source of truth that
    the API polls.
    """

    STATUS_PENDING = "PENDING"
    STATUS_SENT = "SENT"
    STATUS_FAILED = "FAILED"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_SENT, "Sent"),
        (STATUS_FAILED, "Failed"),
    ]

    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, default="")
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)
    sent_at = models.DateTimeField(null=True, blank=True)
    error = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-created_at"]
