import os
import unittest.mock

import pytest

from argocd.services import repository_creds
from tests.services import mocks


@pytest.fixture
def repository_creds_service():
    os.environ["ARGOCD_API_BASE_URL"] = "http://demo.com"
    os.environ["ARGOCD_API_AUTH_TOKEN"] = "dummy_token"

    return repository_creds.RepositoryCredsService()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_creds_list_response,
)
def test_repository_creds_api_list_returns_ok(repository_creds_service):
    response = repository_creds_service.list()

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_creds_list_response,
)
def test_repository_creds_api_list_repo_returns_ok(repository_creds_service):
    response = repository_creds_service.list(repo="dummy_repo")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_list_returns_non_ok(repository_creds_service):
    response = repository_creds_service.list()

    assert isinstance(response, dict)
    assert "error" in response.keys()
