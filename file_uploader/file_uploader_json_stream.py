from minio import Minio
from minio.error import S3Error
import os
import time

def main():
    # Create a client with the MinIO server running locally.
    client = Minio(
        "localhost:9000",  # MinIO endpoint
        access_key="ROOTNAME",
        secret_key="CHANGEME123",
        secure=False
    )

    # The directory which contains the file(s) to upload
    source_directory = "../data/json_batches"
    directory = os.fsencode(source_directory)

    # The destination bucket on the MinIO server
    bucket_name = "python-process-bucket"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Loop through all files within directory, if entry is a file upload it.
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full_file_path = os.path.join(source_directory, filename)
        if os.path.isfile(full_file_path):  # Ensure it's a file, not a directory
            timestamp = int(time.time() * 1000)  # Millisecond timestamp
            destination_file = f"{timestamp}_{filename}"
            client.fput_object(bucket_name, destination_file, full_file_path)
            # Upload the file, renaming it in the process
            print(f"Uploaded: {filename} as {destination_file}. To bucket {bucket_name}")

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)