import pandas as pd
import requests

from .base import StravaBase


class Activities(StravaBase):

    ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"

    # TODO - possible we could add a decorator to check when activity data was been
    # last DLed and only request if there X amount of time has passed since
    def get_activities(self, n: str = 100) -> None:
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
        activities = pd.io.json.json_normalize(activities)

        self.activities = activities
