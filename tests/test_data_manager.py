import os

import pandas as pd
import pytest

from stravaboard.api.access_token import AccessTokenManager
from stravaboard.api.data_manager import ActivitiesManager


@pytest.mark.skipif(
    os.environ.get("STRAVA_CLIENT_ID") == "",
    reason="Strava credentials are not set (e.g. via secrets on GitHub Actions).",
)
def test_ActivitiesManager_retrieves_activities_correctly(
    access_token_manager: AccessTokenManager,
) -> None:
    am = ActivitiesManager()

    assert am.ACTIVITIES_URL == "https://www.strava.com/api/v3/athlete/activities"

    am.get_data(access_token_manager.access_token, n=50)
    am.tidy_data()

    assert isinstance(am.data, pd.DataFrame)
    assert am.data.shape[0] == 50
