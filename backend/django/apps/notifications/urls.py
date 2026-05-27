from django.urls import path

from apps.notifications.api import NotificationListCreateView

urlpatterns = [
    path("", NotificationListCreateView.as_view(), name="notification-list-create"),
]
