import os

import pandas as pd
import pytest
from dotenv import load_dotenv

from stravaboard.api.data_manager import Activities
from stravaboard.api.strava_api import StravaAPI


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_StravaAPI_retrieves_activities_correctly():

    strava_api = StravaAPI(
        client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET_DZ"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
    )

    activities_df = strava_api.get(Activities())

    assert isinstance(activities_df, pd.DataFrame)
    assert activities_df.shape[0] > 1
    assert all(
        col in activities_df.columns for col in ["date", "elapsed_min", "distance_km"]
    )
