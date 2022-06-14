import requests
from pandas.io.json import json_normalize

from .base import StravaBase


class Activities(StravaBase):

    ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"

    def get_activities(self, n: str = 100):

        header = {"Authorization": "Bearer " + self.access_token}
        param = {"per_page": n, "page": 1}
        activities = requests.get(
            self.ACTIVITIES_URL, headers=header, params=param
        ).json()
        activities = json_normalize(activities)

        self.activities = activities
