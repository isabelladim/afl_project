CREATE WAREHOUSE IF NOT EXISTS AFL_WH
  WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 60 AUTO_RESUME = TRUE INITIALLY_SUSPENDED = TRUE;
/* warehouse = small because not large, 
auto_suspend = 60 because we want to save costs, 
auto_resume = true because we want it to automatically resume when we run a query, 
and initially_suspended = true because we don't want it to be running when we're not using it */
CREATE DATABASE IF NOT EXISTS AFL;
CREATE SCHEMA IF NOT EXISTS AFL.RAW;