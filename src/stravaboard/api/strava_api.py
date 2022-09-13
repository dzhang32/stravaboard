import pandas as pd

from stravaboard.api.access_token import AccessTokenManager
from stravaboard.api.data_manager import DataManager


class StravaAPI:
    """Responsible for querying the Strava API."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        data_manager: DataManager,
    ):

        self.access_token_manager = AccessTokenManager(
            client_id, client_secret, refresh_token
        )
        self.data_manager = data_manager

    def get(self) -> pd.DataFrame:
        """Download and tidy Strava data.

        Uses the DataManager to download and tidy the Strava data of interest.

        Returns
        -------
        pd.DataFrame
            _description_
        """
        self.data_manager.get_data(self.access_token_manager.access_token)
        self.data_manager.tidy_data()

        return self.data_manager.data
