import os

from stravaboard.api.access_token import AccessTokenManager


class StravaAPI:

    BASE_URL = "https://www.strava.com/"
    AUTH_URL = os.path.join(BASE_URL, "oauth/token")

    def __init__(self, client_id: str, client_secret: str, refresh_token: str):

        self.access_token_manager = AccessTokenManager(
            client_id, client_secret, refresh_token
        )
