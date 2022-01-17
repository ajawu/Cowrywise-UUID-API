from rest_framework import serializers


class UUIDTimeSerializer(serializers.Serializer):
    uid = serializers.UUIDField()
    timestamp = serializers.DateTimeField()

    def to_representation(self, instance):
        timestamp_without_tz = str(instance.timestamp.replace(tzinfo=None))
        str_uuid = f'{instance.uid}'
        return {timestamp_without_tz: str_uuid}
