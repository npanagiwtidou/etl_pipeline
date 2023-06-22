import os
from datetime import datetime
#from dotenv import load_dotenv
#load_dotenv()

from src.transform import identify_remove_duplicates
from src.load_data_s3 import df_to_s3
from src.extract import extract_transactional_data

# import variables from .env file
dbname=os.getenv('dbname')
host=os.getenv('host')
port=os.getenv('port')
user=os.getenv('user')
password=os.getenv('password')
aws_access_key_id=os.getenv('aws_access_key_id')
aws_secret_access_key=os.getenv('aws_secret_access_key')
aws_s3_bucket=os.getenv('aws_s3_bucket')

start_time=datetime.now()

# Make a connection to redshift, extract and transform
print("Extracting and transforming data in sql")
online_trans_cleaned=extract_transactional_data(dbname, host, port, user, password)

print("Removing duplicated data")
online_trans_deduped=identify_remove_duplicates(online_trans_cleaned)

# Connect and load to S3
print("Loading data to s3")

# Function that writes a data frame as a .csv file to an s3 bucket
key = "bootcamp2/etl/np_online_trans_cleaned.csv"

df_to_s3(online_trans_deduped,key,aws_s3_bucket,aws_access_key_id,aws_secret_access_key)

# this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")