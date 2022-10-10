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


def mocked_failure_version_response(*args, **kwargs):
    class DummyClass:
        def json(self):
            return {
                "code": "1",
                "details": [{"type_url": "http://demo.com", "value": "value"}],
                "error": "Error",
                "message": "Error Message",
            }

    return DummyClass()
