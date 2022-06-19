import pandas as pd
import requests

from .base import StravaBase


class Activities(StravaBase):

    ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"

    # TODO - add a way to check when the activity data was last last_updated
    # similar to StravaBase. However, this is currently handed via StreamLit/@st.cache
    def request_activities(self, n: str = 100) -> None:
        """Obtain DataFrame of Strava activity data

        Queries the Strava API then stores the obtained activity data as a DataFrame
        inside self.activities.

        Parameters
        ----------
        n : str, optional
            the maximum number of activities to retrieve, by default 100
        """
        header = {"Authorization": "Bearer " + self.access_token}
        param = {"per_page": n, "page": 1}
        activities = requests.get(
            self.ACTIVITIES_URL, headers=header, params=param
        ).json()
        activities = pd.json_normalize(activities)

        self.activities = activities

    def tidy_activites(self) -> None:
        """Tidy the activity data."""

        # filter for activites no longer than 24 hours
        # to remove cel's accidental outlier logs
        activities = self.activities.loc[
            (self.activities["sport_type"] == "Run")
            & (self.activities["elapsed_time"] <= (24 * 60 * 60)),
        ].copy()

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

        self.activities = activities[
            [
                "date",
                "elapsed_min",
                "distance_km",
                "speed_mins_per_km",
                "total_elevation_gain",
            ]
        ]

    @property
    def activities(self) -> pd.DataFrame:
        """Getter for the activities property.

        Returns
        -------
        pd.DataFrame
            contains activity data.
        """
        return self._activities

    @activities.setter
    def activities(self, value: pd.DataFrame) -> None:
        """Setter for the activities property.

        Parameters
        ----------
        value : pd.DataFrame
            contains the activity data.

        Raises
        ------
        TypeError
            if the value is not a DataFrame.
        """
        if not isinstance(value, pd.DataFrame):
            raise TypeError("activites must be a DataFrame.")

        self._activities = value
