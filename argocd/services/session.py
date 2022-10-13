from requests import sessions

from argocd import config


class SessionService:
    def __init__(self):
        self.config = config.Config()
        self.session = sessions.Session()

    def create_session(self, password, token, username):
        """
        Create a new JWT for authentication and set a cookie if using HTTP.
        """
        base_url = self.config.server_url
        response = self.session.post(
            f"{base_url}/api/v1/session",
            json={"password": password, "token": token, "username": username},
        )

        return response.json()

    def delete_session(self):
        """
        Delete an existing JWT cookie if using HTTP
        """
        base_url = self.config.server_url
        response = self.session.delete(f"{base_url}/api/v1/session")

        return response.json()

    def me(self):
        """
        Get the current user's info
        """
        base_url = self.config.server_url
        response = self.session.get(f"{base_url}/api/v1/session/userinfo")

        return response.json()
