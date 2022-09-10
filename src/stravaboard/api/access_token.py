from datetime import datetime

import requests

from stravaboard.exceptions import AccessTokenRequestError


class AccessTokenManager:
    """Responsible for retrieving and storing the Strava access token."""

    AUTH_URL = "https://www.strava.com/oauth/token"

    def __init__(self, client_id: str, client_secret: str, refresh_token: str) -> None:
        self.request_access_token(client_id, client_secret, refresh_token)

    def request_access_token(
        self, client_id: str, client_secret: str, refresh_token: str
    ) -> None:
        """Request a Strava access token.

        Obtains an access token from Strava, which is required to send other
        requests (e.g. to get activity data).

        Parameters
        ----------
        client_id : str
            Strava client ID.
        client_secret : str
            Strava client secret.
        refresh_token : str
            Strava refresh token.

        Raises
        ------
        AccessTokenRequestError
            Raised if the request fails (status code != 200).
        """
        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "f": "json",
        }

        res = requests.post(self.AUTH_URL, data=payload, verify=False)

        if res.status_code != 200:
            raise AccessTokenRequestError(
                "Request denied, check your Strava credentials."
            )

        access_token = res.json()["access_token"]

        self.access_token = access_token
        self.last_updated = datetime.now()
