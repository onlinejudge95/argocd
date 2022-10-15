from requests import sessions

from argocd import config


class RepositoryService:
    def __init__(self, token=None):
        self.config = config.Config()
        self.session = sessions.Session()
        self.base_url = self.config.server_url
        token = token or self.config.authentication_token

        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def list(self, repo=None, force_refresh=False):
        """
        ListRepositories gets a list of all configured repositories
        """
        params = {}
        if repo:
            params["repo"] = repo
        if force_refresh:
            params["forceRefresh"] = force_refresh

        response = self.session.get(
            f"{self.base_url}/api/v1/repositories", params=params
        )
        return response.json()

    def create(self, payload, upsert=False, creds_only=False):
        """
        CreateRepository creates a new repository configuration
        """
        params = {}
        if upsert:
            params["upsert"] = upsert
        if creds_only:
            params["credsOnly"] = creds_only

        response = self.session.post(
            f"{self.base_url}/api/v1/repositories", params=params, json=payload
        )
        return response.json()

    def update(self, repo, payload):
        """
        UpdateRepository updates a repository configuration
        """
        response = self.session.put(
            f"{self.base_url}/api/v1/repositories/{repo}", json=payload
        )
        return response.json()

    def get(self, repo, force_refresh=False):
        """
        Get returns a repository or its credentials
        """
        params = {}
        if force_refresh:
            params["forceRefresh"] = force_refresh

        response = self.session.get(
            f"{self.base_url}/api/v1/repositories{repo}", params=params
        )
        return response.json()

    def delete(self, repo, force_refresh=False):
        """
        DeleteRepository deletes a repository from the configuration
        """
        params = {}
        if force_refresh:
            params["forceRefresh"] = force_refresh

        response = self.session.delete(
            f"{self.base_url}/api/v1/repositories{repo}", params=params
        )
        return response.json()

    def list_apps(self, repo, revision=None):
        """
        ListApps returns list of apps in the repo
        """
        params = {}
        if revision:
            params["revision"] = revision

        response = self.session.get(
            f"{self.base_url}/api/v1/repositories/{repo}/apps", params=params
        )
        return response.json()

    def list_charts(self, repo, force_refresh=False):
        """
        GetHelmCharts returns list of helm charts in the specified repository
        """
        params = {}
        if force_refresh:
            params["forceRefresh"] = force_refresh

        response = self.session.get(
            f"{self.base_url}/api/v1/repositories{repo}/helmcharts", params=params
        )
        return response.json()

    def list_refs(self, repo, force_refresh=False):
        """
        RepositoryService_ListRefs
        """
        params = {}
        if force_refresh:
            params["forceRefresh"] = force_refresh

        response = self.session.get(
            f"{self.base_url}/api/v1/repositories{repo}/refs", params=params
        )
        return response.json()

    def validate_access(
        self,
        repo,
        username="",
        password="",
        ssh_private_key="",
        insecure=False,
        tls_client_cert_data="",
        tls_client_cert_key="",
        type="",
        name="",
        enable_oci=False,
        github_app_private_key="",
        github_app_id="",
        github_app_installation_id="",
        github_app_enterprise_base_url="",
        proxy="",
        project="",
    ):
        """
        ValidateAccess validates access to a repository with given parameters
        """
        params = {}
        if username != "":
            params["username"] = username
        if password != "":
            params["password"] = password
        if ssh_private_key != "":
            params["sshPrivateKey"] = ssh_private_key
        if insecure:
            params["insecure"] = insecure
        if tls_client_cert_data != "":
            params["tlsClientCertData"] = tls_client_cert_data
        if tls_client_cert_key != "":
            params["tlsClientCertKey"] = tls_client_cert_key
        if type != "":
            params["type"] = type
        if name != "":
            params["name"] = name
        if enable_oci:
            params["enableOci"] = enable_oci
        if github_app_private_key != "":
            params["githubAppPrivateKey"] = github_app_private_key
        if github_app_id != "":
            params["githubAppID"] = github_app_id
        if github_app_installation_id != "":
            params["githubAppInstallationID"] = github_app_installation_id
        if github_app_enterprise_base_url != "":
            params["githubAppEnterpriseBaseUrl"] = github_app_enterprise_base_url
        if proxy != "":
            params["proxy"] = proxy
        if project != "":
            params["project"] = project
        response = self.session.post(
            f"{self.base_url}/api/v1/repositories{repo}/validate", json=repo
        )
        return response.json()

    def get_app(self, repo, payload):
        """
        GetAppDetails returns application details by given path
        """
        response = self.session.post(
            f"{self.base_url}/api/v1/repositories{repo}/appdetails", json=payload
        )
        return response.json()
