import boto3
import requests
import mimetypes

def upload_file_to_s3(local_file, bucket, object_name=None, acl="private"):
    if object_name is None:
        object_name = local_file
    
    content_type, _ = mimetypes.guess_type(local_file)
    if content_type is None:
        content_type = 'application/octet-stream'  
    with open(local_file, 'rb') as file_data:
        s3_client = boto3.client('s3')
        s3_client.put_object(
            Body=file_data,
            Bucket=bucket,
            Key=object_name,
            ACL=acl,
            ContentType=content_type,
            ContentDisposition='inline'  
        )

def generate_presigned_url(bucket_name, object_name, expires_in=864000):
    s3_client = boto3.client('s3')
    response = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': bucket_name, 'Key': object_name},
                                                ExpiresIn=expires_in)
    return response

if __name__ == "__main__":
    bucket_name = 'ds2002-ycq2zz' 
    local_file = 'chelsea.png' 
    upload_file_to_s3(local_file, bucket_name, acl="public-read")
    presigned_url = generate_presigned_url(bucket_name, local_file)
    print("Presigned URL (valid for 10 days):", presigned_url)
