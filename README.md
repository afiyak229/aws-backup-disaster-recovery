# Automated Backup and Disaster Recovery with AWS S3 and Lambda

## Repository Name
**aws-backup-disaster-recovery**

## Description
This project demonstrates how to automate the backup of critical data to AWS S3 and implement disaster recovery strategies using AWS Lambda and CloudFormation. The aim is to ensure that important data is securely backed up and can be easily restored in case of data loss.

## Key Components
- **Python/Bash Scripts**: Scripts that automate the backup process by uploading files to an S3 bucket.
- **AWS Lambda Function**: A serverless function that monitors the backup process and triggers recovery actions when necessary.
- **CloudFormation Template**: Infrastructure as Code (IaC) that provisions the necessary AWS resources for backup and recovery.



## Prerequisites
Before you begin, ensure you have the following:
- An AWS account
- AWS CLI installed and configured with your credentials
- Basic understanding of AWS services such as S3, Lambda, and CloudFormation
- Python 3.x installed on your local machine

## Setup Instructions
Follow these steps to set up the project:

1. **Create an S3 Bucket**:
   - Go to the [AWS S3 console](https://s3.console.aws.amazon.com/s3).
   - Click on **Create bucket** and specify a unique bucket name.

2. **Create a Lambda Function**:
   - Navigate to the [AWS Lambda console](https://console.aws.amazon.com/lambda).
   - Click on **Create function**, choose **Author from scratch**, and fill in the function name.
   - Set the runtime to Python 3.x and create the function.

3. **Add Lambda Code**:
   - Replace the function code with the provided Python code to monitor backups.
   - Set an environment variable for your S3 bucket name.

4. **Create a Backup Script**:
   - Create a Python script (`backup_script.py`) to automate the backup of files to the S3 bucket. The script should take a local file as input and upload it to S3.

5. **Create a CloudFormation Template**:
   - Write a CloudFormation template (`backup-recovery-template.yaml`) to provision the necessary resources, including the S3 bucket and Lambda function.

6. **Deploy the CloudFormation Stack**:
   - Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).
   - Upload the CloudFormation template to create the necessary resources.

7. **Automate Backups**:
   - Use AWS CloudWatch Events to trigger the Lambda function on a schedule (e.g., hourly).

## Usage
- To manually trigger a backup, run the backup script with the path to your local file:
  ```bash
  export BUCKET_NAME=my-backup-bucket-<your-unique-id>
  python backup_script.py /path/to/your/local/file.txt

