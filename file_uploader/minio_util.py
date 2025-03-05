from minio import Minio
from minio.error import S3Error
import os
import time

def get_minio_client(endpoint="localhost:9000", access_key="ROOTNAME", secret_key="CHANGEME123", secure=False):
    # Create and return a Minio client.
    return Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)

def ensure_bucket(client, bucket_name):
    # Check if a bucket exists on the MinIO server, and create it if it doesn't.
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

def upload_batch_file(client, source_file, bucket_name):
    # Upload a single file to the specified bucket.
    # The file is renamed with a millisecond timestamp to avoid name collisions.
    ensure_bucket(client, bucket_name)
    timestamp = int(time.time() * 1000)
    filename = os.path.basename(source_file)
    destination_file = f"{timestamp}_{filename}"
    client.fput_object(bucket_name, destination_file, source_file)
    print(f"Uploaded: {source_file} successfully uploaded as {destination_file} to bucket {bucket_name}")

def upload_json_files(client, source_directory, bucket_name):
    # Loop through all files in a directory and upload each file to the specified bucket.
    # Each file is renamed with a millisecond timestamp to avoid name collisions.
    ensure_bucket(client, bucket_name)
    directory = os.fsencode(source_directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full_file_path = os.path.join(source_directory, filename)
        if os.path.isfile(full_file_path):
            timestamp = int(time.time() * 1000)
            destination_file = f"{timestamp}_{filename}"
            client.fput_object(bucket_name, destination_file, full_file_path)
            print(f"Uploaded: {filename} as {destination_file} to bucket {bucket_name}")

if __name__ == "__main__":
    try:
        # Initialize the MinIO client.
        client = get_minio_client()

        # Upload a single CSV file.
        csv_source_file = "../data/dummy_data.csv"
        upload_batch_file(client, csv_source_file, "python-batch-bucket")

        # Upload all JSON batch files from a directory.
        json_directory = "../data/json_batches"
        upload_json_files(client, json_directory, "python-process-bucket")

    except S3Error as exc:
        print("Error occurred.", exc)
