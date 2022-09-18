from datetime import datetime

from dotenv import load_dotenv

from stravaboard.api.data_manager import ActivitiesManager

##### Load environmental variables #####

load_dotenv()

##### Main #####

# load and tidy activity data
now = datetime.now().strftime("%d/%m/%Y-%H")

# Stravaboard.display()
"something"
