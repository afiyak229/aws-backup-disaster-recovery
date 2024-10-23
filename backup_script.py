import boto3
import os
import sys

def upload_file_to_s3(local_file, bucket_name, s3_file):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(local_file, bucket_name, s3_file)
        print(f"Upload Successful: {local_file} to {bucket_name}/{s3_file}")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    local_file = sys.argv[1]  # Pass local file as argument
    bucket_name = os.environ['BUCKET_NAME']  # Get from environment variable
    s3_file = os.path.basename(local_file)  # Use the same file name in S3
    upload_file_to_s3(local_file, bucket_name, s3_file)

