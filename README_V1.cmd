## ETL PIPELINE
### Description
This repository contains the implementation of ETL pipeline, as the learning task of extracting,
transforming and loading data during the WAIA bootcamp.

Particularly, the data were extracted from
Redshift warehouse, transformed and loaded to S3 bucket.
The transforming task includes finding and handling missing and
incorrect values,
removing duplicated values, changing datatype and merging datatables.

### Requirements
* The minimum requirements:
  Python 3+

### Instructions on how to execute the code
1. Make sure you are executing the code from the etl_pipeline folder.

2. Install all the libraries you will need to execute main.py.
   - pip3 install -r requirements.txt
3. Copy the .env.example file to .env and fill out the environment vars.

4. Run the main.py script.
   - python3 main.py