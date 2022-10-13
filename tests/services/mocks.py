def mocked_failure_generic_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "code": "1",
                "details": [{"type_url": "http://demo.com", "value": "value"}],
                "error": "Error",
                "message": "Error Message",
            }

    return DummyClass()


def mocked_success_version_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "Version": "v2.5.0+00a1ce6",
                "BuildDate": "2022-10-09T18:23:31Z",
                "GitCommit": "00a1ce6bb2af6e38afc41cdfd415b8540aec4e92",
                "GitTreeState": "clean",
                "GoVersion": "go1.18.7",
                "Compiler": "gc",
                "Platform": "linux/amd64",
                "KustomizeVersion": "v4.5.7 2022-08-02T16:35:54Z",
                "HelmVersion": "v3.10.0+gce66412",
                "KubectlVersion": "v0.24.2",
                "JsonnetVersion": "v0.18.0",
            }

    return DummyClass()


def mocked_success_settings_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "url": "https://cd.apps.argoproj.io",
                "dexConfig": {"connectors": [{"name": "GitHub", "type": "github"}]},
                "appLabelKey": "app.kubernetes.io/instance",
                "resourceOverrides": {
                    "apiextensions.k8s.io/CustomResourceDefinition": {
                        "ignoreDifferences": "jqPathExpressions: null\njsonPointers:\n- /status\n- /spec/preserveUnknownFields\nmanagedFieldsManagers: null\n"  # noqa: E501
                    }
                },
                "statusBadgeEnabled": "true",
                "googleAnalytics": {
                    "trackingID": "UA-123456789-0",
                    "anonymizeUsers": "true",
                },
                "kustomizeOptions": {"BuildOptions": "", "BinaryPath": ""},
                "help": {"chatText": "Chat now!"},
                "plugins": [{"name": "flux"}],
                "userLoginsDisabled": "true",
                "passwordPattern": "^.{8,32}$",
                "trackingMethod": "annotation",
            }

    return DummyClass()


def mocked_success_session_me_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "loggedIn": True,
                "username": "user@example.com",
                "iss": "https://cd.apps.argoproj.io/api/dex",
                "groups": ["groups@example.com"],
            }

    return DummyClass()


def mocked_success_session_create_and_delete_session_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {"token": "secure_token"}

    return DummyClass()
