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


@pytest.fixture
def repository_service_create_payload():
    return {
        "connectionState": {
            "attemptedAt": {"nanos": 0, "seconds": "string"},
            "message": "string",
            "status": "string",
        },
        "enableLfs": True,
        "enableOCI": True,
        "githubAppEnterpriseBaseUrl": "string",
        "githubAppID": "string",
        "githubAppInstallationID": "string",
        "githubAppPrivateKey": "string",
        "inheritedCreds": True,
        "insecure": True,
        "insecureIgnoreHostKey": True,
        "name": "string",
        "password": "string",
        "project": "string",
        "proxy": "string",
        "repo": "string",
        "sshPrivateKey": "string",
        "tlsClientCertData": "string",
        "tlsClientCertKey": "string",
        "type": "string",
        "username": "string",
    }


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_response,
)
def test_repository_api_list_returns_ok(repository_service):
    response = repository_service.list()

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_response,
)
def test_repository_api_list_force_refresh_returns_ok(repository_service):
    response = repository_service.list(force_refresh=True)

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_response,
)
def test_repository_api_list_repo_returns_ok(repository_service):
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
def test_repository_api_list_returns_non_ok(repository_service):
    response = repository_service.list()

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_create_response,
)
def test_repository_api_create_returns_ok(
    repository_service, repository_service_create_payload
):
    response = repository_service.create(repository_service_create_payload)

    assert isinstance(response, dict)
    assert "connectionState" in response.keys()
    assert isinstance(response["connectionState"], dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_create_response,
)
def test_repository_api_create_upsert_returns_ok(
    repository_service, repository_service_create_payload
):
    response = repository_service.create(repository_service_create_payload, upsert=True)

    assert isinstance(response, dict)
    assert "connectionState" in response.keys()
    assert isinstance(response["connectionState"], dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_create_response,
)
def test_repository_api_create_creds_only_returns_ok(
    repository_service, repository_service_create_payload
):
    response = repository_service.create(
        repository_service_create_payload, creds_only=True
    )

    assert isinstance(response, dict)
    assert "connectionState" in response.keys()
    assert isinstance(response["connectionState"], dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_create_returns_non_ok(
    repository_service, repository_service_create_payload
):
    response = repository_service.create(repository_service_create_payload)

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.put",
    mocks.mocked_success_repository_create_response,
)
def test_repository_api_update_returns_ok(
    repository_service, repository_service_create_payload
):
    response = repository_service.update(
        "dummy_repository", repository_service_create_payload
    )

    assert isinstance(response, dict)
    assert "connectionState" in response.keys()
    assert isinstance(response["connectionState"], dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.put",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_update_returns_non_ok(
    repository_service, repository_service_create_payload
):
    response = repository_service.update(
        "dummy_repository", repository_service_create_payload
    )

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_create_response,
)
def test_repository_api_get_returns_ok(repository_service):
    response = repository_service.get("dummy_repository")

    assert isinstance(response, dict)
    assert "connectionState" in response.keys()
    assert isinstance(response["connectionState"], dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_create_response,
)
def test_repository_api_get_force_refresh_returns_ok(repository_service):
    response = repository_service.get("dummy_repository", force_refresh=True)

    assert isinstance(response, dict)
    assert "connectionState" in response.keys()
    assert isinstance(response["connectionState"], dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_get_returns_non_ok(repository_service):
    response = repository_service.get("dummy_repository")

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_delete_returns_ok(repository_service):
    response = repository_service.delete("dummy_repository")

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_delete_force_refresh_returns_ok(repository_service):
    response = repository_service.delete("dummy_repository", force_refresh=True)

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_delete_returns_non_ok(repository_service):
    response = repository_service.delete("dummy_repository")

    assert isinstance(response, dict)
    assert "error" in response.keys()
