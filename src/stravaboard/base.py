import os
from datetime import datetime

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

        self._request_access_token(payload)

    def update_access_token(self, payload: dict) -> None:
        """Update the access token.

        This wraps _request_access_token(). It only requests a new access token if 12
        hours have passed.

        Parameters
        ----------
        payload : dict
            contains the keys "client_id", "client_secret", "refresh_token",
            "grant_type" and "f".
        """
        now = datetime.now()
        duration = now - self.access_token_last_updated
        # update access token only if 12 hours have passed since the last request
        # TODO - turn this into a decorator, though maybe too fancy?
        if duration.total_seconds() >= (12 * 60 * 60):
            self._request_access_token(payload)
        else:
            print("Access token last updated in past 12 hours, no update needed.")

    def _request_access_token(self, payload: dict) -> None:
        """Request the access token.

        This sends a request to Strava to obtain an access token, which is needed to
        send other requests (e.g. to get activity data).

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

        self.access_token = access_token
        self.access_token_last_updated = datetime.now()

    @property
    def access_token(self) -> str:
        """Getter for the access_token property.

        Returns
        -------
        str
            the access token.
        """
        return self._access_token

    @access_token.setter
    def access_token(self, value: str) -> None:
        """Setter for the access_token property.

        Parameters
        ----------
        value : str
            the value you want to set as the access token.
        """
        self._access_token = value

    @property
    def access_token_last_updated(self) -> datetime:
        """Getter for the access_token_last_updated property.

        Returns
        -------
        datetime
            the time the access token was last updated.
        """
        return self._access_token_last_updated

    @access_token_last_updated.setter
    def access_token_last_updated(self, value: datetime) -> None:
        """Setter for the access_token_last_updated property.

        Parameters
        ----------
        value : datetime
            a datetime object, should be created in _request_access_token().

        Raises
        ------
        TypeError
            if the value is not a datetime object.
        """
        if not isinstance(value, datetime):
            raise TypeError("*last_updated attributes must be of type datetime")
        self._access_token_last_updated = value
