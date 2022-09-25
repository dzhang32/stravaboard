import os
from datetime import datetime

import pytest
from dotenv import load_dotenv

from stravaboard.api.access_token import AccessTokenManager
from stravaboard.exceptions import AccessTokenRequestError


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_AccessTokenRequestError_retrieves_access_token_correctly():
    atm = AccessTokenManager(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    assert len(atm.access_token) == 40
    assert isinstance(atm.access_token, str)
    assert isinstance(atm.last_updated, datetime)


def test_AccessTokenManager_errors_on_bad_credentials():
    with pytest.raises(AccessTokenRequestError, match="Strava credentials"):
        AccessTokenManager(
            client_id="a",
            client_secret="b",
            refresh_token="c",
        )
