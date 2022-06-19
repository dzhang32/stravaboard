import os

import pandas as pd
import pytest
from dotenv import load_dotenv

from stravaboard.activities import Activities


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def test_Activities_retrieves_activities_correctly():
    act = Activities(
        client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
        client_secret=os.environ.get("STRAVA_CLIENT_SECRET_DZ"),
        refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
    )

    act.request_activities()

    assert isinstance(act.activities, pd.DataFrame)
    assert act.activities.shape[0] >= 1

    act.tidy_activites()

    assert act.activities.columns.to_list() == [
        "date",
        "elapsed_min",
        "distance_km",
        "speed_mins_per_km",
        "total_elevation_gain",
    ]
