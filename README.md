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
The minimum requirements:

* Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/desktop/install/mac-install/)
* Docker for Windows:
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation steps for older WSL version: [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

### Instructions on how to execute the code
 - Copy the .env.example file to .env and fill out the environment vars.
   
 - Make sure you are executing the code from the etl_pipeline folder and you have Docker Desktop running. 
 - To run it locally first build the image:

   **docker image build -t etl-pipeline:0.1 .**
- Then run the etl job using docker:

  **docker run --env-file .env etl-pipeline:0.1**