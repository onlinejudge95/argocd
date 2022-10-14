import os
import unittest.mock

import pytest

from argocd.services import repository
from tests.services import mocks


@pytest.fixture
def repository_service():
    os.environ["ARGOCD_API_BASE_URL"] = "http://demo.com"
    os.environ["ARGOCD_API_AUTH_TOKEN"] = "dummy_token"

    return repository.RepositoryService()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_response,
)
def test_repository_api_returns_ok(repository_service):
    response = repository_service.list()

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


# TODO:- Write more tests for this API
@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_response,
)
def test_repository_api_force_refresh_returns_ok(repository_service):
    response = repository_service.list(force_refresh=True)

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


# TODO:- Write more tests for this API
@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_response,
)
def test_repository_api_repo_returns_ok(repository_service):
    response = repository_service.list(repo="http://github.com/user/repo")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_returns_non_ok(repository_service):
    response = repository_service.list()

    assert isinstance(response, dict)
    assert "error" in response.keys()
