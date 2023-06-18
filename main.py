import boto3
from pprint import pprint
print("Welcome to S3 uploader and downloader, press 1 for upload and press 2 for download")
choice = int(input())

#FOR UPLOAD
if choice == 1:
    
    print("Insert the path of the file you want to upload: ")
    file=input()

    print("Enter the name by which the file should be uploaded in the bucket: ")
    name = input() 

    s3 = boto3.resource('s3') # Defining the s3 resource

    print("The buckets present in the account are: ")
    for bucket in s3.buckets.all():
        print(bucket.name)

    print("Enter the name of the bucket in which you want to upload the file: ")
    bucket = input()

    try:
        data = open(file,'rb') # Open fucntion is used to open the file and return its contents in a stream
        s3.Bucket(bucket).put_object(Key=name, Body= data) # Uploading the file to the bucket using the name specified by the user
    except:
        print("Error uploading the file")
        
#FOR DOWNLOAD
elif choice == 2:
    
    s3_client = boto3.client('s3') # defining the s3 client
    
    print("The available buckets are:")
    for bucket in s3_client.list_buckets()['Buckets']:
        print(bucket['Name'])
    
    print("Enter a bucket name to view its contents: ")
    download_bucket = input()
    for key in s3_client.list_objects(Bucket=download_bucket)['Contents']:
        print(key['Key'])
    
    print("Enter the name of the object you want to download: ")
    downoad_object = input()
    
    print("Enter the name by which the file should be saved on your device: ")
    download_name= input()
    
    s3_client.download_file(download_bucket, downoad_object, "F:/temp_aws/"+download_name) # Dowloading the specified file from the bucket and storing it in the specified location on the local device
    
        
        

else:
    print("Please enter a valid numnber")