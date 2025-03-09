# How to

## Start containers
> Pre-requisite: Docker installed locally

The Docker Compose file in this project starts the following containers:
- MinIO
- Jupyter Lab/Jupyter Server (Contains environment and all dependencies that are required)

You can start all containers by running the following command: `docker compose up --build`

## Access MinIO GUI
> Pre-requisite: Run docker compose from `Start containers` segment.

- Docker compose exposes localhost:9001 to access the MinIO GUI.
    - Username: `ROOTNAME`
    - Password: `CHANGEME123`

## Access Jupyter Lab (Environment to run everything)
> Pre-requisite: Run docker compose from `Start containers` segment.

- Docker compose exposes localhost:8888, but an access key is needed.
    - URL with access key can be found in the logs once `jupyter-pyspark` container is fully running.

## Create dummy data

### Through Jupyter Notebook
- Open `upload_data_to_minIO.ipynb` within Jupyter Lab and run the segment to create dummy data.

### Through Scripts
- To create a CSV file containing dummy data for batch processing run the following from root of repo:
    - `cd generate_dummy_data`
    - `python generate_dummy_data_csv.py`

- To create multiple JSON files containing dummy data for stream processing run the following from root of repo:
    - `cd generate_dummy_data`
    - `python generate_dummy_data_json.py`


## Upload File(s) to MinIO

### Through Jupyter Notebook
- Open `upload_data_to_minIO.ipynb` within Jupyter Lab and run the segment to upload data.

### Through Scripts
- To upload a CSV file for batch processing run the following from root of repo:
    - `cd file_uploader`
    - `python file_uploader_csv_batch.py`

- To create multiple JSON files containing dummy data for stream processing run the following from root of repo:
    - `cd file_uploader`
    - `python file_uploader_json_stream.py`
