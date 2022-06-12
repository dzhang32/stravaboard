import os

import requests


class StravaBase:
    BASE_URL = "https://www.strava.com/"
    AUTH_URL = os.path.join(BASE_URL, "oauth/token")

    def __init__(self, client_id, client_secret, refresh_token):

        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "f": "json",
        }

        self.get_auth_token(payload)

    def get_auth_token(self, payload):
        res = requests.post(self.AUTH_URL, data=payload, verify=False)
        access_token = res.json()["access_token"]

        self.access_token = access_token
