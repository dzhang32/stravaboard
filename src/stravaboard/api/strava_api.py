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
    ):
        self.access_token_manager = AccessTokenManager(
            client_id, client_secret, refresh_token
        )

    def get(self, data_manager: DataManager) -> pd.DataFrame:
        """Download and tidy Strava data.

        Uses a DataManager class object to download and tidy the Strava data of
        interest.

        Parameters
        ----------
        data_manager : DataManager
            an object that manages the querying and tidying of a specific type
            of Strava data.

        Returns
        -------
        pd.DataFrame
            contains tidy Strava data.
        """
        data_manager.get_data(self.access_token_manager.access_token)
        data_manager.tidy_data()

        return data_manager.data
