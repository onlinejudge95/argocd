from requests import sessions

from argocd import config


class RepositoryCredsService:
    def __init__(self, token=None):
        self.config = config.Config()
        self.session = sessions.Session()
        self.base_url = self.config.server_url
        token = token or self.config.authentication_token

        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def list(self, repo=""):
        """
        ListRepositoryCredentials gets a list of all configured
        repository credential sets
        """
        params = {}
        if repo != "":
            params["repo"] = repo

        response = self.session.get(f"{self.base_url}/api/v1/repocreds", params=params)
        return response.json()

    def create(self, payload, upsert=False):
        """
        CreateRepositoryCredentials creates a new repository credential set
        """
        params = {}
        if upsert:
            params["upsert"] = upsert

        response = self.session.post(
            f"{self.base_url}/api/v1/repocreds", params=params, json=payload
        )
        return response.json()

    def update(self, creds, payload):
        """
        UpdateRepositoryCredentials updates a repository credential set
        """
        response = self.session.put(
            f"{self.base_url}/api/v1/repocreds/{creds}", json=payload
        )
        return response.json()

    def delete(self, creds):
        """
        DeleteRepositoryCredentials deletes a repository credential set
        from the configuration
        """
        response = self.session.delete(f"{self.base_url}/api/v1/repocreds/{creds}")
        return response.json()
