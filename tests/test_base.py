import os

import pytest
from dotenv import load_dotenv

from stravaboard.base import StravaBase
from stravaboard.exceptions import StravaRequestError


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_StravaBase_retrieves_access_token_correctly():
    sb = StravaBase(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    assert len(sb.access_token) == 40
    assert isinstance(sb.access_token, str)


def test_StravaBase_errors_on_bad_credentials():
    with pytest.raises(StravaRequestError, match="Strava credentials"):
        StravaBase(
            client_id=os.environ.get("STRAVA_CLIENT_ID"),
            client_secret="not_a_client_secret",
            refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
        )
