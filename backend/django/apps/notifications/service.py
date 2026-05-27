from apps.notifications.models import NotificationModel
from apps.notifications.tasks.send_notification import send_notification


def notification_create(*, recipient: str, subject: str, body: str) -> NotificationModel:
    notification = NotificationModel.objects.create(
        recipient=recipient,
        subject=subject,
        body=body,
        status=NotificationModel.STATUS_PENDING,
    )
    send_notification.delay(str(notification.id))
    return notification
