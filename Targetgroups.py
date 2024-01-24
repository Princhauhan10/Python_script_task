import boto3
import time
import re

def create_target_group(elbv2_client, vpc_id, protocol, port):
    # Create Target Group
    target_group_name = f'tg-{int(time.time())}'  # Generating a unique but compliant name
    target_group_name = re.sub('[^a-zA-Z0-9-]', '', target_group_name)[:32]  # Remove invalid characters and truncate

    response_target_group = elbv2_client.create_target_group(
        Name=target_group_name,
        Protocol=protocol,
        Port=port,
        VpcId=vpc_id,
        HealthCheckProtocol=protocol,
        HealthCheckPort=str(port),
        HealthCheckPath='/',
        HealthCheckIntervalSeconds=30,
        HealthCheckTimeoutSeconds=5,
        HealthyThresholdCount=5,
        UnhealthyThresholdCount=2,
    )

    print(f"Target Group {target_group_name} created.")
    return target_group_name


def list_target_group_names(elbv2_client):
    # List only Target Group names
    target_group_details = elbv2_client.describe_target_groups()
    target_group_names = [target_group['TargetGroupName'] for target_group in target_group_details['TargetGroups']]
    return target_group_names

def describe_target_group(elbv2_client, target_group_name):
    # Describe Target Group details using TargetGroupNames
    response = elbv2_client.describe_target_groups(Names=[target_group_name])

    # Print Target Group details
    print("\nTarget Group Details:")
    for group in response['TargetGroups']:
        print(f"Target Group Name: {group['TargetGroupName']}")
        print(f"Target Group ARN: {group['TargetGroupArn']}")
        print(f"Protocol: {group['Protocol']}")
        print(f"Port: {group['Port']}")
        print(f"VPC ID: {group['VpcId']}")
        print(f"Health Check Protocol: {group['HealthCheckProtocol']}")
        print(f"Health Check Port: {group['HealthCheckPort']}")
        print(f"Health Check Path: {group['HealthCheckPath']}")
        print(f"Health Check Interval: {group['HealthCheckIntervalSeconds']} seconds")
        print(f"Health Check Timeout: {group['HealthCheckTimeoutSeconds']} seconds")
        print(f"Healthy Threshold Count: {group['HealthyThresholdCount']}")
        print(f"Unhealthy Threshold Count: {group['UnhealthyThresholdCount']}")


def delete_target_group(elbv2_client, target_group_arn):
    # Delete Target Group using TargetGroupArn
    response = elbv2_client.delete_target_group(TargetGroupArn=target_group_arn)

    print(f"Target Group {target_group_arn} deleted.")


if __name__ == "__main__":
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '####'
    secret_key = '###'
    region = 'us-east-2'

    elbv2_client = boto3.client('elbv2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    while True:
        # Create multiple Target Groups
        vpc_id = 'vpc-**********'  # Replace with your VPC ID
        protocol = 'HTTP'  # Replace with your desired protocol (e.g., HTTP, HTTPS)
        port = 80  # Replace with your desired port

        target_group_name = create_target_group(elbv2_client, vpc_id, protocol, port)

        # List Target Group names
        target_group_names = list_target_group_names(elbv2_client)
        print("\nList of Target Group Names:")
        for name in target_group_names:
            print(name)

        # Choose a Target Group to get details
        target_group_name_to_get_details = input("\nEnter the Target Group Name to get details (or press Enter to skip): ").strip()
        if target_group_name_to_get_details:
            describe_target_group(elbv2_client, target_group_name_to_get_details)

        # Choose a Target Group to delete
        delete_option = input("\nDo you want to delete a Target Group? (yes/no): ").strip().lower()
        if delete_option == 'yes':
            target_group_name_to_delete = input("Enter the Target Group Name to delete: ").strip()
            delete_target_group(elbv2_client, target_group_name_to_delete)

        exit_option = input("\nDo you want to exit the loop? (yes/no): ").strip().lower()
        if exit_option == 'yes' or not target_group_names:
            break
