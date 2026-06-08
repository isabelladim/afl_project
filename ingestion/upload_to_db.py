from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv
from sqlalchemy.engine import URL
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

def upload_to_postgres(df, table_name, engine) -> None:
    df.to_sql(table_name, engine, schema="raw", if_exists='replace', index=False)

def create_db_engine():
    port_number = os.environ["DB_PORT"]
    db_host = os.environ["DB_HOST"]
    db_name = os.environ["DATABASE_NAME"]
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASSWORD"]

    connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=db_user,
    password=db_password,  
    host=db_host,
    port=port_number,
    database=db_name)

    logger.info("Created database engine with URL: %s", connection_url)
    return create_engine(connection_url)
    

def main():
    engine = create_db_engine()
    year = 2026
    team_ID = 15 #St Kilda
    datasets = {
        "games": API_connection.get_team_games(year, team_ID, user_agent),
        "ladder": API_connection.get_afl_info("ladder", year, user_agent),
        "teams": API_connection.get_afl_info("teams", year, user_agent),
        "tips": API_connection.get_afl_info("tips", year, user_agent)
    }

    for table_name, data in datasets.items():
        upload_to_postgres(data, table_name, engine)        #load data into postgres
        logger.info("Loaded %s rows into raw.%s", len(data), table_name)

if __name__ == "__main__":
    main()