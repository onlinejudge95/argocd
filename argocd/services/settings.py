from argocd.services import _base


class SettingsService(_base.BaseService):
    def get_server_settings(self):
        """
        Returns the settings information from the argo cd API server.
        """
        response = self.session.get(f"{self.base_url}/api/v1/settings")

        return response.json()
