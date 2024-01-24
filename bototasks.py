'''import boto3
import time
import pytz
from datetime import datetime

def create_ec2_instance():
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '########'
    secret_key = '########'
    region = 'us-east-1'

    # Connect to AWS
    ec2_client = boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Specify instance details
    instance_type = 't2.micro'
    ami_id = 'ami-##########'  # Replace with your desired AMI ID
    security_group_id = 'sg-#########'  # Replace with your security group ID

    # Launch EC2 instance without specifying key pair
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        SecurityGroupIds=[security_group_id],
        MinCount=1,
        MaxCount=1
    )

    # Get instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} created.")

    # Wait for the instance to be running
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    print("Instance is now running.")

    # Get instance details
    instance_details = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_info = instance_details['Reservations'][0]['Instances'][0]

    # Convert launch time to IST
    launch_time_utc = instance_info['LaunchTime']
    launch_time_utc = launch_time_utc.replace(tzinfo=pytz.utc)
    launch_time_ist = launch_time_utc.astimezone(pytz.timezone('Asia/Kolkata'))

    # Print instance details with IST launch time
    print("Instance Details:")
    print(f"Instance ID: {instance_id}")
    print(f"Instance Type: {instance_info['InstanceType']}")
    print(f"Launch Time (UTC): {launch_time_utc}")
    print(f"Launch Time (IST): {launch_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Simulate some time passing (you may want to perform other actions or wait for user input)
    time.sleep(60)

    # Terminate the instance
    ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} terminated.")

if __name__ == "__main__":
    create_ec2_instance()
'''
'''
#dynamic parameters
import boto3
import time
import pytz

def create_ec2_instances(num_instances):
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '##$'
    secret_key = '###'
    region = 'us-east-1'

    # Connect to AWS
    ec2_client = boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Specify instance details
    instance_type = 't2.micro'
    ami_id = 'ami-##########'  # Replace with your desired AMI ID
    security_group_id = 'sg-##########'  # Replace with your security group ID

    instance_ids = []

    # Create multiple instances
    for _ in range(num_instances):
        response = ec2_client.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            SecurityGroupIds=[security_group_id],
            MinCount=1,
            MaxCount=1
        )

        # Get instance ID and add to the list
        instance_id = response['Instances'][0]['InstanceId']
        instance_ids.append(instance_id)
        print(f"Instance {instance_id} created.")

    return instance_ids

def list_instances(ec2_client):
    # List all instances
    instances = ec2_client.describe_instances()
    print("\nList of Instances:")
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"Launch Time (UTC): {instance['LaunchTime']}")
            print("---------------------")

def get_instance_details(ec2_client, instance_id):
    # Get details of a specific instance
    instance_details = ec2_client.describe_instances(InstanceIds=[instance_id])
    if 'Reservations' in instance_details and instance_details['Reservations']:
        instance_info = instance_details['Reservations'][0]['Instances'][0]

        # Convert launch time to IST
        launch_time_utc = instance_info['LaunchTime']
        launch_time_utc = launch_time_utc.replace(tzinfo=pytz.utc)
        launch_time_ist = launch_time_utc.astimezone(pytz.timezone('Asia/Kolkata'))

        # Print instance details with IST launch time
        print("\nInstance Details:")
        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_info['InstanceType']}")
        print(f"Launch Time (UTC): {launch_time_utc}")
        print(f"Launch Time (IST): {launch_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    else:
        print(f"Instance with ID {instance_id} not found.")

def terminate_instances(ec2_client, instance_ids):
    # Terminate instances
    if instance_ids:
        terminate_response = ec2_client.terminate_instances(InstanceIds=instance_ids)
        print("Instances terminated:")
        for instance in terminate_response['TerminatingInstances']:
            print(f"Instance ID: {instance['InstanceId']}")
    else:
        print("No instances to terminate.")

if __name__ == "__main__":
    num_instances = 2  # Change this value to create a different number of instances
    instances_created = create_ec2_instances(num_instances)

    ec2_client = boto3.client('ec2', region_name='us-east-1', aws_access_key_id='$#$#', aws_secret_access_key='@##@')

    list_instances(ec2_client)

    # Choose an instance to get details
    instance_id_to_get_details = input("\nEnter the Instance ID to get details (or press Enter to skip): ").strip()
    if instance_id_to_get_details:
        get_instance_details(ec2_client, instance_id_to_get_details)

    # Choose instances to terminate
    terminate_option = input("\nDo you want to terminate instances? (yes/no): ").strip().lower()
    if terminate_option == 'yes':
        terminate_all_option = input("Do you want to terminate all instances? (yes/no): ").strip().lower()

        if terminate_all_option == 'yes':
            terminate_instances(ec2_client, instances_created)
        else:
            instances_to_terminate = input("Enter instance IDs to terminate (comma-separated): ").strip().split(',')
            terminate_instances(ec2_client, instances_to_terminate)
'''
#use below code


import boto3
import time
import pytz

def create_ec2_instances(num_instances):
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '####'
    secret_key = '###'
    region = 'us-east-1'

    # Connect to AWS
    ec2_client = boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Specify instance details
    instance_type = 't2.micro'
    ami_id = 'ami-###############3'  # Replace with your desired AMI ID
    security_group_id = 'sg-#############3'  # Replace with your security group ID

    instance_ids = []

    # Create multiple instances
    for _ in range(num_instances):
        response = ec2_client.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            SecurityGroupIds=[security_group_id],
            MinCount=1,
            MaxCount=1
        )

        # Get instance ID and add to the list
        instance_id = response['Instances'][0]['InstanceId']
        instance_ids.append(instance_id)
        print(f"Instance {instance_id} created.")

    return instance_ids

def list_instance_ids(ec2_client):
    # List only instance IDs
    instances = ec2_client.describe_instances()
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_ids.append(instance_id)
    return instance_ids

def get_instance_details(ec2_client, instance_id):
    # Get details of a specific instance
    instance_details = ec2_client.describe_instances(InstanceIds=[instance_id])
    if 'Reservations' in instance_details and instance_details['Reservations']:
        instance_info = instance_details['Reservations'][0]['Instances'][0]

        # Convert launch time to IST
        launch_time_utc = instance_info['LaunchTime']
        launch_time_utc = launch_time_utc.replace(tzinfo=pytz.utc)
        launch_time_ist = launch_time_utc.astimezone(pytz.timezone('Asia/Kolkata'))

        # Print instance details with IST launch time
        print("\nInstance Details:")
        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_info['InstanceType']}")
        print(f"State: {instance_info['State']['Name']}")
        print(f"Public IP: {instance_info.get('PublicIpAddress', 'N/A')}")
        print(f"Private IP: {instance_info.get('PrivateIpAddress', 'N/A')}")
        print(f"Launch Time (UTC): {launch_time_utc}")
        print(f"Launch Time (IST): {launch_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    else:
        print(f"Instance with ID {instance_id} not found.")

def terminate_instances(ec2_client, instance_ids):
    # Terminate instances
    if instance_ids:
        terminate_response = ec2_client.terminate_instances(InstanceIds=instance_ids)
        print("Instances terminated:")
        for instance in terminate_response['TerminatingInstances']:
            print(f"Instance ID: {instance['InstanceId']}")
        return True
    else:
        print("No instances to terminate.")
        return False

if __name__ == "__main__":
    num_instances = 2  # Change this value to create a different number of instances
    instances_created = create_ec2_instances(num_instances)

    ec2_client = boto3.client('ec2', region_name='us-east-1', aws_access_key_id='###', aws_secret_access_key='####')

    while True:
        # List only instance IDs
        instance_ids = list_instance_ids(ec2_client)
        print("\nList of Instance IDs:")
        for instance_id in instance_ids:
            print(instance_id)

        # Choose an instance to get details
        instance_id_to_get_details = input("\nEnter the Instance ID to get details (or press Enter to skip): ").strip()
        if instance_id_to_get_details:
            get_instance_details(ec2_client, instance_id_to_get_details)

        # Choose instances to terminate
        terminate_option = input("\nDo you want to terminate instances? (yes/no): ").strip().lower()
        if terminate_option == 'yes':
            terminate_all_option = input("Do you want to terminate all instances? (yes/no): ").strip().lower()

            if terminate_all_option == 'yes':
                terminated = terminate_instances(ec2_client, instances_created)
                if terminated:
                    break
            else:
                instances_to_terminate = input("Enter instance IDs to terminate (comma-separated): ").strip().split(',')
                terminated = terminate_instances(ec2_client, instances_to_terminate)
                if terminated:
                    break

        exit_option = input("\nDo you want to exit the loop? (yes/no): ").strip().lower()
        if exit_option == 'yes':
            break


