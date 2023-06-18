# aws-s3-upload-download
This is a command line tool to upload and download files to and from AWS S3 buckets. It uses Python and boto3.
Instructions:
- Download the AWS CLI.
- Open the ~/.aws/credentials file (%USERPROFILE%\.aws\credentials for windows) and paste your access key and access key ID as follows:\n
[default]\n
aws_access_key_id = ACCESS_KEY_ID\n
aws_secret_access_key = SECRET_ACCESS_KEY\n

- Now go to ~/.aws/configure file (%USERPROFILE%\.aws\config for windows) and paste the default region as follows:
[default]\n
region = ap-south-1\n

- Now run the main.py file and follow the on-screen instructions

