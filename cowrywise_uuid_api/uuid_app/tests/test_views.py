import random

from django.urls import reverse
from rest_framework.test import APIClient

from cowrywise_uuid_api.utils.uuid_app.helpers import response_matches
from cowrywise_uuid_api.uuid_app.models import UUIDTime


class TestUUIDs:
    url = reverse('uuid-list')

    def test_create_field(self, client: APIClient) -> None:
        count = UUIDTime.objects.count()
        response = client.get(self.url)
        new_count = UUIDTime.objects.count()
        assert response.status_code == 200
        assert count < new_count

    def test_only_one_field_created(self, client: APIClient) -> None:
        count = UUIDTime.objects.count()
        response = client.get(self.url)
        new_count = UUIDTime.objects.count()
        assert response.status_code == 200
        assert new_count - count == 1

    def test_response_format_matches_question(self, client: APIClient) -> None:
        response = client.get(self.url)
        assert response.status_code == 200
        assert all(map(response_matches, response.data))

    def test_previous_fields_saved(self, client: APIClient) -> None:
        count = UUIDTime.objects.count()
        call_times = random.randint(1, 20)
        for iterate in range(call_times):
            client.get(self.url)
        new_count = UUIDTime.objects.count()
        assert count + call_times == new_count
