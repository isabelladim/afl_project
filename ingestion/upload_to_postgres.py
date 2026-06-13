from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import logging
import os 
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def upload_to_postgres(df, table_name, engine) -> None:
    df.to_sql(table_name, engine, schema="raw", if_exists='replace', index=False)

def create_postgres_engine():
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