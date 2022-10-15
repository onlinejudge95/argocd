from requests import sessions

from argocd import config


class CertificateService:
    def __init__(self, token=None):
        self.config = config.Config()
        self.session = sessions.Session()
        self.base_url = self.config.server_url
        token = token or self.config.authentication_token

        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def list(self, host_name_pattern="", cert_type="", cert_sub_type=""):
        """
        List all available repository certificates
        """
        params = {}
        if host_name_pattern:
            params["hostNamePattern"] = host_name_pattern
        if cert_type:
            params["certYype"] = cert_type
        if cert_sub_type:
            params["certSubType"] = cert_sub_type

        response = self.session.get(
            f"{self.base_url}/api/v1/certificates", params=params
        )
        return response.json()

    def create(self, payload, upsert=False):
        """
        Creates repository certificates on the server
        """
        params = {}
        if upsert:
            params["upsert"] = upsert

        response = self.session.post(
            f"{self.base_url}/api/v1/certificates", params=params, json=payload
        )
        return response.json()

    def delete(self, host_name_pattern="", cert_type="", cert_sub_type=""):
        """
        Delete the certificates that match the RepositoryCertificateQuery
        """
        params = {}
        if host_name_pattern:
            params["hostNamePattern"] = host_name_pattern
        if cert_type:
            params["certYype"] = cert_type
        if cert_sub_type:
            params["certSubType"] = cert_sub_type

        response = self.session.delete(
            f"{self.base_url}/api/v1/certificates", params=params
        )
        return response.json()
