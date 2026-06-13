import os
import pandas as pd
import snowflake.connector.pandas_tools
import snowflake
from dotenv import load_dotenv
import logging

def get_snowflake_connection():
    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        role="ACCOUNTADMIN",               
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database=os.environ["SNOWFLAKE_DATABASE"],
        schema="RAW",
    )


def upload_to_snowflake(records, table_name, conn) -> None:
    df = pd.DataFrame(records)
    df.columns = df.columns.str.upper() #upper column names to match snowflake convention
    success, nchunks, nrows, _ = snowflake.connector.pandas_tools.write_pandas(conn=conn, df=df, table_name=table_name, schema="RAW", quote_identifiers=False,auto_create_table=True, overwrite=True)
    if success:
        logging.info("Successfully uploaded %d rows to Snowflake table %s", nrows, table_name)
    else:
        logging.error("Failed to upload data to Snowflake table %s", table_name)
