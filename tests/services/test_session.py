import os
import unittest.mock

import pytest

from argocd.services import session
from tests.services import mocks


@pytest.fixture
def session_service():
    os.environ["ARGOCD_API_BASE_URL"] = "http://demo.com"
    return session.SessionService()


@unittest.mock.patch(
    "argocd.services.session.sessions.Session.get",
    mocks.mocked_success_session_me_response,
)
def test_session_api_me_returns_ok(session_service):
    response = session_service.me()

    assert isinstance(response, dict)
    assert "username" in response
    assert "groups" in response
    assert isinstance(response["groups"], list)


@unittest.mock.patch(
    "argocd.services.session.sessions.Session.get",
    mocks.mocked_failure_generic_response,
)
def test_session_api_me_returns_non_ok(session_service):
    response = session_service.me()

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.session.sessions.Session.post",
    mocks.mocked_success_session_create_and_delete_session_response,
)
def test_session_api_create_session_returns_ok(session_service):
    response = session_service.create_session("password", "token", "username")

    assert isinstance(response, dict)
    assert "token" in response.keys()
    assert isinstance(response["token"], str)


@unittest.mock.patch(
    "argocd.services.session.sessions.Session.post",
    mocks.mocked_failure_generic_response,
)
def test_session_api_create_session_returns_not_ok(session_service):
    response = session_service.create_session("password", "token", "username")

    assert isinstance(response, dict)
    assert "error" in response.keys()


@unittest.mock.patch(
    "argocd.services.session.sessions.Session.delete",
    mocks.mocked_success_session_create_and_delete_session_response,
)
def test_session_api_delete_session_returns_ok(session_service):
    response = session_service.delete_session()

    assert isinstance(response, dict)
    assert "token" in response.keys()
    assert isinstance(response["token"], str)


@unittest.mock.patch(
    "argocd.services.session.sessions.Session.delete",
    mocks.mocked_failure_generic_response,
)
def test_session_api_delete_session_returns_not_ok(session_service):
    response = session_service.delete_session()

    assert isinstance(response, dict)
    assert "error" in response.keys()
