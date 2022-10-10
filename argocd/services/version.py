from requests import sessions

from argocd import config


class VersionService:
    def __init__(self):
        self.config = config.Config()
        self.session = sessions.Session()

    def get_server_version(self):
        """
        Returns the version information from the argo cd API server.
        """
        base_url = self.config.server_url
        response = self.session.get(f"{base_url}/api/version")

        return response.json()
