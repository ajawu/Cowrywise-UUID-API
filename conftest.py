import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db) -> None:  # type: ignore
    pass
