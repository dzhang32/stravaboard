from abc import ABC, abstractmethod

import pandas as pd
import requests


class DataManager(ABC):
    @abstractmethod
    def get_data(self) -> None:
        pass

    @abstractmethod
    def tidy_data(self) -> None:
        pass


class ActivitiesManager(DataManager):
    """Responsible for requesting and storing activities data."""

    ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"

    def get_data(self, access_token: str, n: int = 200) -> None:
        """Download Strava activity data.

        Queries the Strava API then stores the obtained activity data as a
        DataFrame inside self.data.

        Parameters
        ----------
        access_token : str
            Strava access token.
        n : int, optional
            the maximum number of activities to retrieve, by default 200
        """
        header = {"Authorization": "Bearer " + access_token}
        params = {"per_page": n, "page": 1}
        activities = requests.get(
            self.ACTIVITIES_URL, headers=header, params=params
        ).json()
        activities = pd.json_normalize(activities)

        self.data = activities

    def tidy_data(self) -> None:
        """Tidy the activity data.

        Convert speed, distance, time and date columns to interpretable units
        of measurement.
        """
        activities = self.data

        activities["elapsed_min"] = round(activities["elapsed_time"] / 60, 2)
        activities["distance_km"] = round(activities["distance"] / 1000, 2)
        activities["speed_mins_per_km"] = round(
            (activities["elapsed_min"] / activities["distance_km"]), 2
        )
        activities["date"] = activities["start_date_local"].str.replace(
            "T.*", "", regex=True
        )
        activities["date"] = pd.to_datetime(
            activities["date"], infer_datetime_format=True
        )

        self.data = activities
