## ETL PIPELINE
### Description
This repository contains the implementation of ETL pipeline, as the learning task of extracting,
transforming and loading data during the WAIA bootcamp.

Particularly, the data were extracted from
Redshift warehouse, transformed and loaded to S3 bucket.
The transforming task includes finding and handling missing and
incorrect values,
removing duplicated values, changing datatype and merging datatables.

### Requirements (using python)
* The minimum requirements using python:
  **Python 3+**

### Instructions on how to execute the code
1. Make sure you are executing the code from the etl_pipeline folder.
2. Open the requirements.txt and add "dotenv" library. Totally, 4 libraries should be included in the requirements.txt
   - psycopg2-binary
   - pandas
   - boto3
   - dotenv

3. Install all the libraries you will need to execute main.py.
   
   **- pip3 install -r requirements.txt**
4. Copy the .env.example file to .env and fill out the environment vars.
5. In the "main.py" remove the comments in the following lines:
   
   #from dotenv import load_dotenv

   #load_dotenv()
6. Run the main.py script.

   **- python3 main.py**