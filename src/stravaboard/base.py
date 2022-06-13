import os

import requests

from stravaboard.exceptions import StravaRequestError


class StravaBase:
    BASE_URL = "https://www.strava.com/"
    AUTH_URL = os.path.join(BASE_URL, "oauth/token")

    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "f": "json",
        }

        self.refresh_access_token(payload)

    def refresh_access_token(self, payload: dict):
        """Refresh the access token.

        This reobtains the access token, which is helpful if it's expired.

        Parameters
        ----------
        payload : dict
            contains the keys "client_id", "client_secret", "refresh_token",
            "grant_type" and "f".

        Raises
        ------
        StravaRequestError
            Raised if the request fails (status code != 200).
        """
        res = requests.post(self.AUTH_URL, data=payload, verify=False)

        if res.status_code != 200:
            raise StravaRequestError("Request denied, check your Strava credentials.")

        access_token = res.json()["access_token"]

        self._access_token = access_token

    @property
    def access_token(self) -> str:
        """Getter for the access token property.

        Returns
        -------
        str
            the access token.
        """
        return self._access_token

    @access_token.setter
    def access_token(self, value: str) -> None:
        """Setter for the access token property.

        Parameters
        ----------
        value : str
            the value you want to set as the access token.
        """
        self.access_token = value
