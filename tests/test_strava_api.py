import os

import pandas as pd
import pytest

from stravaboard.api.strava_api import StravaAPI
from stravaboard.exceptions import InvalidDataTypeError


def test_StravaAPI_retrieves_activities_correctly() -> None:
    strava_api = StravaAPI(
        client_id=os.environ.get("STRAVA_CLIENT_ID"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN"),
    )

    # Check that invalid data types raise an error.
    with pytest.raises(InvalidDataTypeError, match="data_type must be one of:"):
        strava_api.get("invalid_data_type")

    # Check that the activities data is retrieved correctly.
    activities_df = strava_api.get("activities")

    assert isinstance(activities_df, pd.DataFrame)
    assert activities_df.shape[0] > 1
    assert all(
        col in activities_df.columns for col in ["date", "elapsed_min", "distance_km"]
    )
