import os

import pandas as pd
import pytest
from dotenv import load_dotenv

from stravaboard.api.strava_api import StravaAPI
from stravaboard.exceptions import InvalidDataTypeError


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_StravaAPI_retrieves_activities_correctly():

    strava_api = StravaAPI(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    with pytest.raises(InvalidDataTypeError, match="data_type must be one of:"):
        strava_api.get("invalid_data_type")

    activities_df = strava_api.get("activities")

    assert isinstance(activities_df, pd.DataFrame)
    assert activities_df.shape[0] > 1
    assert all(
        col in activities_df.columns for col in ["date", "elapsed_min", "distance_km"]
    )
