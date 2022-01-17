from typing import Any

from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from .models import UUIDTime
from .serializer import UUIDTimeSerializer


class UUIDTimeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = UUIDTime.objects.all()
    serializer_class = UUIDTimeSerializer

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
            Creates a new UUID field and returns all UUID fields including the newly created one.
        """
        UUIDTime.objects.create()
        return super(UUIDTimeViewSet, self).list(request, *args, **kwargs)
