import os

from dotenv import load_dotenv

from stravaboard.streamlit.components import Summary
from stravaboard.streamlit.stravaboard import Stravaboard

# load strava credentials from .env
load_dotenv()


sb = Stravaboard(
    client_id=os.environ.get("STRAVA_CLIENT_ID_DZ"),
    client_secret=os.environ.get("STRAVA_CLIENT_SECRET_DZ"),
    refresh_token=os.environ.get("STRAVA_REFRESH_TOKEN_DZ"),
)
sb.display(components=[Summary])
