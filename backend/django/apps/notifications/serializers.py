from rest_framework import serializers

from apps.notifications.models import NotificationModel


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = ["id", "recipient", "subject", "body", "status", "sent_at", "error", "created_at"]
        read_only_fields = ["id", "status", "sent_at", "error", "created_at"]


class NotificationCreateSerializer(serializers.Serializer):
    recipient = serializers.CharField(max_length=255)
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField(allow_blank=True, default="")
