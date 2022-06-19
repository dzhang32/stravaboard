import os
from datetime import datetime

import pytest
from dotenv import load_dotenv

from stravaboard.base import StravaBase
from stravaboard.exceptions import StravaRequestError


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_StravaBase_retrieves_access_token_correctly(capfd):
    sb = StravaBase(
        client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET_DZ"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
    )

    assert len(sb.access_token) == 40
    assert isinstance(sb.access_token, str)
    assert isinstance(sb.access_token_last_updated, datetime)
    with pytest.raises(TypeError, match="must be of type datetime"):
        sb.access_token_last_updated = "a_str"

    # payload here should NOT be used, so set to arbitrary values
    # if payload was used, would raise StravaRequestError
    payload = {
        "client_id": "x",
        "client_secret": "y",
        "refresh_token": "z",
        "grant_type": "a",
        "f": "b",
    }
    sb.update_access_token(payload)
    out, _ = capfd.readouterr()
    assert "no update needed." in out


def test_StravaBase_errors_on_bad_credentials():
    with pytest.raises(StravaRequestError, match="Strava credentials"):
        StravaBase(
            client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
            client_secret="not_a_client_secret",
            refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
        )
