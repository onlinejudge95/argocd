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
