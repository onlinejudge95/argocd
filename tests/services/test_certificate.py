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


@unittest.mock.patch(
    "argocd.services.repository.sessions.Session.get",
    mocks.mocked_success_repository_creds_list_response,
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
    mocks.mocked_success_repository_creds_list_response,
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
    mocks.mocked_success_repository_creds_list_response,
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
    mocks.mocked_success_repository_creds_list_response,
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
