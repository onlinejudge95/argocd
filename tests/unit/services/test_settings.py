import os
import unittest.mock

import pytest

from argocd.services import settings
from tests.unit.services import mocks


@pytest.fixture
def settings_service():
    os.environ["ARGOCD_API_BASE_URL"] = "http://demo.com"
    os.environ["ARGOCD_API_AUTH_TOKEN"] = "dummy_token"
    return settings.SettingsService()


@unittest.mock.patch(
    "argocd.services.base.sessions.Session.get",
    mocks.mocked_success_settings_response,
)
def test_settings_api_returns_ok(settings_service):
    response = settings_service.get_server_settings()

    assert isinstance(response, dict)
    assert "url" in response.keys()


@unittest.mock.patch(
    "argocd.services.base.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_settings_api_returns_non_ok(settings_service):
    response = settings_service.get_server_settings()

    assert isinstance(response, dict)
    assert "error" in response.keys()
