class AccessTokenManager:
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "f": "json",
        }

        self._request_access_token(payload)
