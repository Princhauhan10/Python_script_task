'''import boto3
import time
import pytz
from datetime import datetime

def create_elb():
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '########'
    secret_key = '##########'
    region = 'us-east-1'

    # Connect to AWS
    elbv2_client = boto3.client('elbv2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Specify load balancer details
    load_balancer_name = 'my-load-balancer'
    subnets = ['subnet-############', 'subnet-###############']  # Replace with your subnet IDs
    security_groups = ['sg-################']  # Replace with your security group IDs

    # Create a load balancer
    response = elbv2_client.create_load_balancer(
        Name=load_balancer_name,
        Subnets=subnets,
        SecurityGroups=security_groups,
        Scheme='internet-facing',
        Tags=[
            {
                'Key': 'Name',
                'Value': 'MyLoadBalancer'
            },
        ]
    )

    # Get load balancer ARN
    load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']
    print(f"Load Balancer {load_balancer_arn} created.")

    # Wait for the load balancer to be active
    waiter = elbv2_client.get_waiter('load_balancer_exists')
    waiter.wait(Names=[load_balancer_name])
    print("Load Balancer is now active.")

    # Describe load balancer details
    load_balancer_details = elbv2_client.describe_load_balancers(Names=[load_balancer_name])
    load_balancer_info = load_balancer_details['LoadBalancers'][0]

    # Convert creation time to IST
    creation_time_utc = load_balancer_info['CreatedTime']
    creation_time_utc = creation_time_utc.replace(tzinfo=pytz.utc)
    creation_time_ist = creation_time_utc.astimezone(pytz.timezone('Asia/Kolkata'))

    # Print load balancer details with IST creation time
    print("Load Balancer Details:")
    print(f"Load Balancer ARN: {load_balancer_info['LoadBalancerArn']}")
    print(f"DNS Name: {load_balancer_info['DNSName']}")
    print(f"Scheme: {load_balancer_info['Scheme']}")
    print(f"Creation Time (UTC): {creation_time_utc}")
    print(f"Creation Time (IST): {creation_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Simulate some time passing (you may want to perform other actions or wait for user input)
    time.sleep(60)

    # Delete the load balancer
    elbv2_client.delete_load_balancer(LoadBalancerArn=load_balancer_arn)
    print(f"Load Balancer {load_balancer_arn} deleted.")

if __name__ == "__main__":
    create_elb()
'''

import boto3
import time
import pytz

def create_elb(elbv2_client, name, subnets, security_groups):
    # Create a load balancer
    response = elbv2_client.create_load_balancer(
        Name=name,
        Subnets=subnets,
        SecurityGroups=security_groups,
        Scheme='internet-facing',
        Tags=[
            {
                'Key': 'Name',
                'Value': 'MyLoadBalancer'
            },
        ]
    )

    # Get load balancer ARN
    load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']
    print(f"Load Balancer {name} created.")

    # Wait for the load balancer to be active
    waiter = elbv2_client.get_waiter('load_balancer_exists')
    waiter.wait(Names=[name])
    print("Load Balancer is now active.")

    return load_balancer_arn

def list_elb_names(elbv2_client):
    # List only load balancer names
    load_balancers = elbv2_client.describe_load_balancers()
    load_balancer_names = [lb['LoadBalancerName'] for lb in load_balancers['LoadBalancers']]
    return load_balancer_names

def get_elb_details(elbv2_client, name):
    # Describe load balancer details
    load_balancer_details = elbv2_client.describe_load_balancers(Names=[name])
    if 'LoadBalancers' in load_balancer_details and load_balancer_details['LoadBalancers']:
        load_balancer_info = load_balancer_details['LoadBalancers'][0]

        # Convert creation time to IST
        creation_time_utc = load_balancer_info['CreatedTime']
        creation_time_utc = creation_time_utc.replace(tzinfo=pytz.utc)
        creation_time_ist = creation_time_utc.astimezone(pytz.timezone('Asia/Kolkata'))

        # Print load balancer details with IST creation time
        print("\nLoad Balancer Details:")
        print(f"Load Balancer ARN: {load_balancer_info['LoadBalancerArn']}")
        print(f"DNS Name: {load_balancer_info['DNSName']}")
        print(f"Scheme: {load_balancer_info['Scheme']}")
        print(f"Creation Time (UTC): {creation_time_utc}")
        print(f"Creation Time (IST): {creation_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    else:
        print(f"Load Balancer with name {name} not found.")

def delete_elb(elbv2_client, load_balancer_arn):
    # Delete the load balancer
    elbv2_client.delete_load_balancer(LoadBalancerArn=load_balancer_arn)
    print(f"Load Balancer {load_balancer_arn} deleted.")

if __name__ == "__main__":
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '#####'
    secret_key = '#####'
    region = 'us-east-1'

    elbv2_client = boto3.client('elbv2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    while True:
        # Create multiple load balancers
        num_elbs = 2  # Change this value to create a different number of load balancers
        for i in range(num_elbs):
            name = f'my-load-balancer-{i+1}'
            subnets = ['subnet-###########', 'subnet-##############']  # Replace with your subnet IDs
            security_groups = ['sg-###############']  # Replace with your security group IDs
            create_elb(elbv2_client, name, subnets, security_groups)

        # List load balancer names
        load_balancer_names = list_elb_names(elbv2_client)
        print("\nList of Load Balancer Names:")
        for lb_name in load_balancer_names:
            print(lb_name)

        # Choose a load balancer to get details
        lb_name_to_get_details = input("\nEnter the Load Balancer Name to get details (or press Enter to skip): ").strip()
        if lb_name_to_get_details:
            get_elb_details(elbv2_client, lb_name_to_get_details)

        # Choose a load balancer to delete
        delete_option = input("\nDo you want to delete a load balancer? (yes/no): ").strip().lower()
        if delete_option == 'yes':
            lb_name_to_delete = input("Enter the Load Balancer Name to delete: ").strip()
            lb_arn_to_delete = create_elb(elbv2_client, lb_name_to_delete, subnets, security_groups)
            delete_elb(elbv2_client, lb_arn_to_delete)

        exit_option = input("\nDo you want to exit the loop? (yes/no): ").strip().lower()
        if exit_option == 'yes':
            break
