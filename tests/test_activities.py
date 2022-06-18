import os

import pandas as pd
import pytest
from dotenv import load_dotenv

from stravaboard.activities import Activities


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_Activities_retrieves_access_token_correctly():
    act = Activities(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    act.get_activities()

    assert isinstance(act.activities, pd.DataFrame)
