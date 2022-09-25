import os

import pandas as pd
import pytest
from dotenv import load_dotenv

from stravaboard.api.access_token import AccessTokenManager
from stravaboard.api.data_manager import ActivitiesManager


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def access_token():
    atm = AccessTokenManager(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    return atm.access_token


def test_ActivitiesManager_retrieves_activities_correctly(access_token):

    am = ActivitiesManager()

    assert am.ACTIVITIES_URL == "https://www.strava.com/api/v3/athlete/activities"

    am.get_data(access_token, n=50)
    am.tidy_data()

    assert isinstance(am.data, pd.DataFrame)
    assert am.data.shape[0] == 50
