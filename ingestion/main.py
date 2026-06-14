import os 
from dotenv import load_dotenv
import upload_to_snowflake
from upload_to_snowflake import get_snowflake_connection, upload_to_snowflake
import logging
import API_connection 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

#load env file
load_dotenv()
user_agent = os.environ["SQUIGGLE_USER_AGENT"]

def main():
    engion = get_snowflake_connection() #connect to snowflake
    year = 2026
    datasets = {
        "GAMES": API_connection.get_afl_info("games", year, user_agent),
        "STANDINGS": API_connection.get_afl_info("standings", year, user_agent),
        "LADDER": API_connection.get_afl_info("ladder", year, user_agent),
        "TEAMS": API_connection.get_afl_info("teams", year, user_agent),
        "TIPS": API_connection.get_afl_info("tips", year, user_agent)
    }

    for table_name, data in datasets.items():
        upload_to_snowflake(data, table_name, engion)   #load data into snowflake
        logger.info("Loaded %s rows into raw.%s", len(data), table_name)

if __name__ == "__main__":
    main()