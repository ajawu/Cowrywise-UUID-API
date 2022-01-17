import uuid

from django.db import models


class UUIDTime(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'UUID: {self.uid}'

    class Meta:
        db_table = 'uuid_time'
        ordering = ['-timestamp']
