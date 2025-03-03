# How to
## Create dummy data

- To create a CSV file containing dummy data for batch processing run the following from root of repo:
    - `cd generate_dummy_data`
    - `python generate_dummy_data_csv.py`

- To create multiple JSON files containing dummy data for stream processing run the following from root of repo:
    - `cd generate_dummy_data`
    - `python generate_dummy_data_json.py`


## Upload File(s) to MinIO

- To upload a CSV file for batch processing run the following from root of repo:
    - `cd file_uploader`
    - `python file_uploader_csv_batch.py`

- To create multiple JSON files containing dummy data for stream processing run the following from root of repo:
    - `cd file_uploader`
    - `python file_uploader_json_stream.py`