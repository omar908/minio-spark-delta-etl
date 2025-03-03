from minio import Minio
from minio.error import S3Error
import time
import os

def main():
    # Create a client with the MinIO server running locally.
    client = Minio(
        "localhost:9000",  # MinIO endpoint
        access_key="ROOTNAME",
        secret_key="CHANGEME123",
        secure=False
    )

    # The file to upload
    source_file = "../data/dummy_data.csv"

    # The destination bucket on the MinIO server
    bucket_name = "python-batch-bucket"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    timestamp = int(time.time() * 1000)  # Millisecond timestamp
    filename = os.path.basename(source_file)
    destination_file = f"{timestamp}_{filename}"
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(f"Uploaded: {source_file} successfully uploaded as {destination_file}. To bucket {bucket_name}")

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)