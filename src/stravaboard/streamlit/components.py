from abc import ABC, abstractmethod
from datetime import datetime

from dateutil.relativedelta import relativedelta

import streamlit as st


class StravaboardComponent(ABC):
    @staticmethod
    @abstractmethod
    def display() -> None:
        pass


class Summary(StravaboardComponent):
    @staticmethod
    def display(activities) -> None:

        st.write(
            "You've run a total of ",
            str(round(activities["distance_km"].sum(), 2)),
            "km over ",
            str(round(activities["elapsed_min"].sum() / 60, 2)),
            " hours 🥳",
        )

        total_across = st.radio(
            "Across the last _____, that's: ", ("week", "month", "year")
        )

        if total_across == "week":
            date_delta = relativedelta(days=7)
        elif total_across == "month":
            date_delta = relativedelta(months=1)
        else:
            date_delta = relativedelta(years=1)

        latest_date = datetime.now()
        total_across_df = activities.loc[
            activities["date"] > (latest_date - date_delta)
        ]
        total_km = total_across_df["distance_km"].sum()
        total_hours = round(total_across_df["elapsed_min"].sum() / 60, 2)

        st.write(str(total_km), "km and ", str(total_hours), " hours 💪")
