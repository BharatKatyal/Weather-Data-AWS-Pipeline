import boto3
import os
from dotenv import load_dotenv

def cleanup_s3():
    # Load environment variables
    load_dotenv()
    bucket_name = os.getenv('AWS_BUCKET_NAME')
    
    if not bucket_name:
        print("Error: AWS_BUCKET_NAME not found in .env file")
        return

    # Confirm with user
    confirmation = input(f"Are you sure you want to delete the S3 bucket '{bucket_name}'? (yes/no): ")
    
    if confirmation.lower() != 'yes':
        print("Operation cancelled")
        return

    try:
        # Initialize S3 client
        s3_client = boto3.client('s3')
        
        # Delete all objects in bucket first
        print(f"Deleting all objects in bucket {bucket_name}...")
        bucket = boto3.resource('s3').Bucket(bucket_name)
        bucket.objects.all().delete()
        
        # Delete the bucket
        print(f"Deleting bucket {bucket_name}...")
        s3_client.delete_bucket(Bucket=bucket_name)
        
        print(f"Successfully deleted bucket {bucket_name}")
        
    except Exception as e:
        print(f"Error deleting bucket: {str(e)}")

if __name__ == "__main__":
    cleanup_s3()