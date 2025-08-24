from datetime import datetime

import requests

from stravaboard.exceptions import AccessTokenRequestError, MissingCredentialsError


class AccessTokenManager:
    """
    Responsible for retrieving and storing the Strava access token.
    """

    AUTH_URL = "https://www.strava.com/oauth/token"

    def __init__(
        self,
        client_id: str | None,
        client_secret: str | None,
        refresh_token: str | None,
    ) -> None:
        self.request_access_token(client_id, client_secret, refresh_token)

    def request_access_token(
        self,
        client_id: str | None,
        client_secret: str | None,
        refresh_token: str | None,
    ) -> None:
        """
        Request a Strava access token.

        Obtains an access token from Strava, which is required to send other requests
        (e.g. to get activity data). See the usage section in the README for how to
        obtain the Strava client ID, client secret, and refresh token.

        Args:
            client_id: Strava client ID.
            client_secret: Strava client secret.
            refresh_token: Strava refresh token.

        Raises:
            AccessTokenRequestError: Raised if the request fails (status code != 200).
        """
        if client_id is None or client_secret is None or refresh_token is None:
            raise MissingCredentialsError(
                "Client ID, client secret, and refresh token must be provided."
            )

        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "f": "json",
        }

        res = requests.post(self.AUTH_URL, data=payload)

        if res.status_code != 200:
            raise AccessTokenRequestError(
                "Request denied, check your Strava credentials."
            )

        access_token = res.json()["access_token"]

        self.access_token = access_token
        self.last_updated = datetime.now()
