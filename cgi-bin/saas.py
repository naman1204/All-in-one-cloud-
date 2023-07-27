import boto3

s3 = boto3.client('s3')

def upload():
    
    filename = 'untitled'  # replace with your file name
    bucket_name = 'saas.upload'  # replace with your bucket name

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, filename)

