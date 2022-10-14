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
