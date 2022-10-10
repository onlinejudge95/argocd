import os
import unittest.mock

import pytest

from argopy.services import version
from tests.services import mocks


@pytest.fixture
def version_service():
    os.environ["ARGOCD_API_BASE_URL"] = "http://demo.com"
    return version.VersionService()


@unittest.mock.patch(
    "argopy.services.version.sessions.Session.get",
    mocks.mocked_success_version_response,
)
def test_version_api_returns_ok(version_service):
    response = version_service.get_server_version()

    assert isinstance(response, dict)
    assert "Version" in response.keys()


@unittest.mock.patch(
    "argopy.services.version.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_version_api_returns_non_ok(version_service):
    response = version_service.get_server_version()

    assert isinstance(response, dict)
    assert "error" in response.keys()
