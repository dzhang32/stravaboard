import pandas as pd

from stravaboard.api.access_token import AccessTokenManager
from stravaboard.api.data_manager import ActivitiesManager
from stravaboard.exceptions import InvalidDataTypeError


class StravaAPI:
    """Responsible for querying the Strava API."""

    DATA_TYPES = {"activities": ActivitiesManager()}

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ):
        self.access_token_manager = AccessTokenManager(
            client_id, client_secret, refresh_token
        )

    def get(self, data_type: str) -> pd.DataFrame:
        """Download and tidy Strava data.

        Parameters
        ----------
        data_type : str
            the type of Strava data to download, must be "activities".

        Returns
        -------
        pd.DataFrame
            contains tidy Strava data.
        """
        if data_type not in self.DATA_TYPES:
            available_types = ", ".join(self.DATA_TYPES.keys())
            raise InvalidDataTypeError(f"data_type must be one of: {available_types}")

        data_manager = self.DATA_TYPES[data_type]
        data_manager.get_data(self.access_token_manager.access_token)
        data_manager.tidy_data()

        return data_manager.data
