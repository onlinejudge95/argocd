from argocd.services import _base


class VersionService(_base.BaseService):
    def get_server_version(self):
        """
        Returns the version information from the argo cd API server.
        """
        response = self.session.get(f"{self.base_url}/api/version")

        return response.json()
