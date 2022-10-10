from requests import sessions

from argocd import config


class SettingsService:
    def __init__(self):
        self.config = config.Config()
        self.session = sessions.Session()

    def get_server_settings(self):
        """
        Returns the settings information from the argo cd API server.
        """
        base_url = self.config.server_url
        response = self.session.get(f"{base_url}/api/v1/settings")

        return response.json()
