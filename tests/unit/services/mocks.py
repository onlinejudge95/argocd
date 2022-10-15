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


def mocked_success_repository_list_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "metadata": {},
                "items": [
                    {
                        "repo": "https://github.com/user/repo",
                        "username": "user@example.com",
                        "connectionState": {
                            "status": "Successful",
                            "message": "",
                            "attemptedAt": "2022-10-14T05:01:04Z",
                        },
                        "type": "git",
                    }
                ],
            }

    return DummyClass()


def mocked_success_repository_create_response(*args, **kwargs):
    class DummyClass:
        def json(self):
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

    return DummyClass()


def mocked_success_repository_delete_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return dict()

    return DummyClass()


def mocked_success_repository_list_apps_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {"items": [{"path": "string", "type": "string"}]}

    return DummyClass()


def mocked_success_repository_list_charts_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {"items": [{"name": "string", "versions": ["string"]}]}

    return DummyClass()


def mocked_success_repository_list_refs_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {"branches": ["string"], "tags": ["string"]}

    return DummyClass()


def mocked_success_repository_get_app_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "directory": {},
                "helm": {
                    "fileParameters": [{"name": "string", "path": "string"}],
                    "name": "string",
                    "parameters": [
                        {"forceString": True, "name": "string", "value": "string"}
                    ],
                    "valueFiles": ["string"],
                    "values": "string",
                },
                "ksonnet": {
                    "environments": {
                        "property1": {
                            "destination": {"namespace": "string", "server": "string"},
                            "k8sVersion": "string",
                            "name": "string",
                        },
                        "property2": {
                            "destination": {"namespace": "string", "server": "string"},
                            "k8sVersion": "string",
                            "name": "string",
                        },
                    },
                    "name": "string",
                    "parameters": [
                        {"component": "string", "name": "string", "value": "string"}
                    ],
                },
                "kustomize": {"images": ["string"]},
                "type": "string",
            }

    return DummyClass()


def mocked_success_repository_creds_list_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "items": [
                    {
                        "enableOCI": True,
                        "githubAppEnterpriseBaseUrl": "string",
                        "githubAppID": "string",
                        "githubAppInstallationID": "string",
                        "githubAppPrivateKey": "string",
                        "password": "string",
                        "sshPrivateKey": "string",
                        "tlsClientCertData": "string",
                        "tlsClientCertKey": "string",
                        "type": "string",
                        "url": "string",
                        "username": "string",
                    }
                ],
                "metadata": {
                    "continue": "string",
                    "remainingItemCount": "string",
                    "resourceVersion": "string",
                    "selfLink": "string",
                },
            }

    return DummyClass()


def mocked_success_repository_creds_create_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "enableOCI": True,
                "githubAppEnterpriseBaseUrl": "string",
                "githubAppID": "string",
                "githubAppInstallationID": "string",
                "githubAppPrivateKey": "string",
                "password": "string",
                "sshPrivateKey": "string",
                "tlsClientCertData": "string",
                "tlsClientCertKey": "string",
                "type": "string",
                "url": "string",
                "username": "string",
            }

    return DummyClass()


def mocked_success_certificate_response(*args, **kwargs):
    class DummyClass:
        def json(self):
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

    return DummyClass()
