#!/bin/bash

BUCKET_NAME="ds2002-ycq2zz" 
read -p "Enter the URL of the file to download and upload to S3: " FILE_URL

FILE_NAME=$(basename "$FILE_URL")

curl "$FILE_URL" > "$FILE_NAME"

if [ -f "$FILE_NAME" ]; then
    echo "File downloaded successfully: $FILE_NAME"
    
    MIME_TYPE=$(file --brief --mime-type "$FILE_NAME")
    aws s3 cp "$FILE_NAME" "s3://$BUCKET_NAME/" --content-type "$MIME_TYPE"
    
    PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$FILE_NAME" --expires-in 604800)
    
    echo "Presigned URL (valid for 10 days): $PRESIGNED_URL"
else
    echo "Failed to download the file."
fi
