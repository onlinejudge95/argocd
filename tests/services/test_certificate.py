import os
import unittest.mock

import pytest

from argocd.services import certificate
from tests.services import mocks


@pytest.fixture
def certificate_service():
    os.environ["ARGOCD_API_BASE_URL"] = "http://demo.com"
    os.environ["ARGOCD_API_AUTH_TOKEN"] = "dummy_token"

    return certificate.CertificateService()


@pytest.fixture
def certificate_service_create_payload():
    return {
        "items": [
            {
                "certData": "string",
                "certInfo": "string",
                "certSubType": "string",
                "certType": "string",
                "serverName": "string",
            }
        ],
        "metadata": {
            "continue": "string",
            "remainingItemCount": "string",
            "resourceVersion": "string",
            "selfLink": "string",
        },
    }


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_list_returns_ok(certificate_service):
    response = certificate_service.list()

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_list_host_name_pattern_returns_ok(
    certificate_service,
):
    response = certificate_service.list(host_name_pattern="dummy_host_name_pattern")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_list_cert_type_returns_ok(
    certificate_service,
):
    response = certificate_service.list(cert_type="dummy_cert_type")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_list_cert_sub_type_returns_ok(
    certificate_service,
):
    response = certificate_service.list(cert_sub_type="dummy_cert_sub_type")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_repository_certificate_api_list_returns_not_ok(certificate_service):
    response = certificate_service.list()

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_create_returns_ok(
    certificate_service, certificate_service_create_payload
):
    response = certificate_service.create(certificate_service_create_payload)

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_create_upsert_returns_ok(
    certificate_service, certificate_service_create_payload
):
    response = certificate_service.create(
        certificate_service_create_payload, upsert=True
    )

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.post",
    mocks.mocked_failure_generic_response,
)
def test_repository_certificate_api_create_returns_not_ok(
    certificate_service, certificate_service_create_payload
):
    response = certificate_service.create(certificate_service_create_payload)

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_delete_returns_ok(certificate_service):
    response = certificate_service.delete()

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_delete_host_name_pattern_returns_ok(
    certificate_service,
):
    response = certificate_service.delete(host_name_pattern="dummy_host_name_pattern")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_delete_cert_type_returns_ok(certificate_service):
    response = certificate_service.delete(cert_type="dummy_cert_type")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_success_certificate_response,
)
def test_repository_certificate_api_delete_cert_sub_type_returns_ok(
    certificate_service,
):
    response = certificate_service.delete(cert_sub_type="dummy_cert_sub_type")

    assert isinstance(response, dict)
    assert isinstance(response["items"], list)
    assert "items" in response.keys()
    assert isinstance(response["metadata"], dict)
    assert "metadata" in response.keys()


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.delete",
    mocks.mocked_failure_generic_response,
)
def test_repository_certificate_api_delete_returns_not_ok(certificate_service):
    response = certificate_service.delete()

    assert isinstance(response, dict)
    assert "error" in response.keys()
