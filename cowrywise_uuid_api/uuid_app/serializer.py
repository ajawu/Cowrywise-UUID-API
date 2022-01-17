from rest_framework import serializers


class UUIDTimeSerializer(serializers.Serializer):
    uid = serializers.UUIDField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance: 'UUIDTimeSerializer') -> dict[str, str]:
        timestamp_without_tz = str(instance.timestamp.replace(tzinfo=None))  # type: ignore
        str_uuid = f'{instance.uid}'
        return {timestamp_without_tz: str_uuid}
