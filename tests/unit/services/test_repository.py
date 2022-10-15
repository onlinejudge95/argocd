import os
import unittest.mock

import pytest

from argocd.services import repository
from tests.unit.services import mocks


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


@pytest.fixture
def repository_service_get_app_payload():
    return {
        "appName": "string",
        "source": {
            "chart": "string",
            "directory": {
                "exclude": "string",
                "include": "string",
                "jsonnet": {
                    "extVars": [{"code": True, "name": "string", "value": "string"}],
                    "libs": ["string"],
                    "tlas": [{"code": True, "name": "string", "value": "string"}],
                },
                "recurse": True,
            },
            "helm": {
                "fileParameters": [{"name": "string", "path": "string"}],
                "parameters": [
                    {"forceString": True, "name": "string", "value": "string"}
                ],
                "passCredentials": True,
                "releaseName": "string",
                "valueFiles": ["string"],
                "values": "string",
                "version": "string",
            },
            "ksonnet": {
                "environment": "string",
                "parameters": [
                    {"component": "string", "name": "string", "value": "string"}
                ],
            },
            "kustomize": {
                "commonAnnotations": {"property1": "string", "property2": "string"},
                "commonLabels": {"property1": "string", "property2": "string"},
                "forceCommonAnnotations": True,
                "forceCommonLabels": True,
                "images": ["string"],
                "namePrefix": "string",
                "nameSuffix": "string",
                "version": "string",
            },
            "path": "string",
            "plugin": {
                "env": [{"name": "string", "value": "string"}],
                "name": "string",
            },
            "repoURL": "string",
            "targetRevision": "string",
        },
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


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_apps_response,
)
def test_repository_api_list_apps_returns_ok(repository_service):
    response = repository_service.list_apps("dummy_repository")

    assert isinstance(response, dict)
    assert "items" in response.keys()
    assert isinstance(response["items"], list)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_apps_response,
)
def test_repository_api_list_apps_revision_returns_ok(repository_service):
    response = repository_service.list_apps("dummy_repository", revision="123")

    assert isinstance(response, dict)
    assert "items" in response.keys()
    assert isinstance(response["items"], list)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_list_apps_returns_non_ok(repository_service):
    response = repository_service.list_apps("dummy_repository")

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_charts_response,
)
def test_repository_api_list_charts_return_ok(repository_service):
    response = repository_service.list_charts("dummy_repository")

    assert isinstance(response, dict)
    assert "items" in response.keys()
    assert isinstance(response["items"], list)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_charts_response,
)
def test_repository_api_list_charts_force_refresh_return_ok(repository_service):
    response = repository_service.list_charts("dummy_repository", force_refresh=True)

    assert isinstance(response, dict)
    assert "items" in response.keys()
    assert isinstance(response["items"], list)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_list_charts_return_non_ok(repository_service):
    response = repository_service.list_charts("dummy_repository")

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_refs_response,
)
def test_repository_api_list_refs_return_ok(repository_service):
    response = repository_service.list_refs("dummy_repository")

    assert isinstance(response, dict)
    assert "branches" in response.keys()
    assert isinstance(response["branches"], list)
    assert isinstance(response["branches"][0], str)
    assert "tags" in response.keys()
    assert isinstance(response["tags"], list)
    assert isinstance(response["tags"][0], str)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_list_refs_response,
)
def test_repository_api_list_refs_force_refresh_return_ok(repository_service):
    response = repository_service.list_refs("dummy_repository", force_refresh=True)

    assert isinstance(response, dict)
    assert "branches" in response.keys()
    assert isinstance(response["branches"], list)
    assert isinstance(response["branches"][0], str)
    assert "tags" in response.keys()
    assert isinstance(response["tags"], list)
    assert isinstance(response["tags"][0], str)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_list_refs_return_non_ok(repository_service):
    response = repository_service.list_refs("dummy_repository")

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_get_app_response,
)
def test_repository_api_get_app_return_ok(
    repository_service, repository_service_get_app_payload
):
    response = repository_service.get_app(
        "dummy_repository", repository_service_get_app_payload
    )

    assert isinstance(response, dict)
    assert "directory" in response.keys()
    assert isinstance(response["directory"], dict)
    assert isinstance(response["type"], str)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_get_app_return_non_ok(
    repository_service, repository_service_get_app_payload
):
    response = repository_service.get_app(
        "dummy_repository", repository_service_get_app_payload
    )

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_return_ok(repository_service):
    response = repository_service.validate_access("dummy_repository")

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_username_return_ok(repository_service):
    response = repository_service.validate_access(
        "dummy_repository", username="dummy_username"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_password_return_ok(repository_service):
    response = repository_service.validate_access(
        "dummy_repository", password="dummy_password"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_ssh_private_key_return_ok(repository_service):
    response = repository_service.validate_access(
        "dummy_repository", ssh_private_key="dummy_ssh_private_key"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_insecure_return_ok(repository_service):
    response = repository_service.validate_access("dummy_repository", insecure=True)

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_tls_client_cert_data_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository", tls_client_cert_data="dummy_tls_client_cert_data"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_tls_client_cert_key_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository", tls_client_cert_key="dummy_tls_client_cert_key"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_type_return_ok(repository_service):
    response = repository_service.validate_access("dummy_repository", type="dummy_type")

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_name_return_ok(repository_service):
    response = repository_service.validate_access("dummy_repository", name="dummy_name")

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_enable_oci_return_ok(
    repository_service,
):
    response = repository_service.validate_access("dummy_repository", enable_oci=True)

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_github_app_private_key_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository", github_app_private_key="dummy_github_app_private_key"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_github_app_id_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository", github_app_id="dummy_github_app_id"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_github_app_installation_id_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository",
        github_app_installation_id="dummy_github_app_installation_id",
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_github_app_enterprise_base_url_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository",
        github_app_enterprise_base_url="dummy_github_app_enterprise_base_url",
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_proxy_return_ok(repository_service):
    response = repository_service.validate_access(
        "dummy_repository", proxy="dummy_proxy"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_repository_delete_response,
)
def test_repository_api_validate_access_project_return_ok(
    repository_service,
):
    response = repository_service.validate_access(
        "dummy_repository", project="dummy_project"
    )

    assert isinstance(response, dict)


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_failure_generic_response,
)
def test_repository_api_validate_access_return_non_ok(repository_service):
    response = repository_service.validate_access("dummy_repository")

    assert isinstance(response, dict)
    assert "error" in response.keys()
