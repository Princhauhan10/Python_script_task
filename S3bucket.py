import boto3
import time

def create_s3_buckets(bucket_names, region, access_key, secret_key):
    s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    for bucket_name in bucket_names:
        # Append a unique timestamp to the bucket name
        unique_bucket_name = f"{bucket_name}-{int(time.time())}"

        # Specify the region when creating the S3 bucket
        s3_client.create_bucket(Bucket=unique_bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"S3 Bucket {unique_bucket_name} created.")



def list_s3_buckets(region, access_key, secret_key):
    s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = s3_client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

def display_bucket_details(bucket_name, region, access_key, secret_key):
    s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    try:
        bucket_details = s3_client.head_bucket(Bucket=bucket_name)
        print(f"\nDetails for S3 Bucket {bucket_name}:")
        print(f"Creation Date: {bucket_details['ResponseMetadata']['HTTPHeaders']['date']}")
        print(f"Region: {bucket_details['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region']}")
    except Exception as e:
        print(f"Error fetching details for S3 Bucket {bucket_name}: {str(e)}")

def delete_s3_bucket(bucket_name, region, access_key, secret_key):
    s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"S3 Bucket {bucket_name} deleted.")
    except Exception as e:
        print(f"Error deleting S3 Bucket {bucket_name}: {str(e)}")

if __name__ == "__main__":
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '#########'
    secret_key = '###################'
    region = 'us-east-2'

    # Specify the names of the buckets you want to create
    bucket_names = ['bucket1', 'bucket2', 'bucket3']

    # Create S3 buckets
    create_s3_buckets(bucket_names, region, access_key, secret_key)

    try:
        while True:
            print("\nList of S3 Buckets:")
            buckets = list_s3_buckets(region, access_key, secret_key)
            for index, bucket in enumerate(buckets, start=1):
                print(f"{index}. {bucket}")

            choice = input("\nEnter the number of the bucket to display details (or 'exit' to exit): ")
            if choice.lower() == 'exit':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(buckets):
                selected_bucket = buckets[int(choice) - 1]
                display_bucket_details(selected_bucket, region, access_key, secret_key)

                delete_choice = input("\nDo you want to delete this bucket? (yes/no): ")
                if delete_choice.lower() == 'yes':
                    delete_s3_bucket(selected_bucket, region, access_key, secret_key)
            else:
                print("Invalid choice. Please enter a valid number or 'exit'.")
    except KeyboardInterrupt:
        print("\nOperation aborted by the user.")
    finally:
        print("Exiting the script.")
