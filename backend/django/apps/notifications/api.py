from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.notifications.models import NotificationModel
from apps.notifications.serializers import NotificationCreateSerializer, NotificationSerializer
from apps.notifications.service import notification_create


class NotificationListCreateView(ListCreateAPIView):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request: Request, *args: object, **kwargs: object) -> Response:
        serializer = NotificationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = notification_create(**serializer.validated_data)
        return Response(NotificationSerializer(notification).data, status=status.HTTP_202_ACCEPTED)
