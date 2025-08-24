import os

import pytest
from dotenv import load_dotenv

from stravaboard.api.access_token import AccessTokenManager


# autouse=True means that the fixture will be run for every test in the module.
@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    """
    Load the STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, and STRAVA_REFRESH_TOKEN
    from the .env file.
    """
    load_dotenv()


@pytest.fixture
def access_token_manager() -> AccessTokenManager:
    """
    Create an AccessTokenManager and return the access token.
    """
    atm = AccessTokenManager(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    return atm
