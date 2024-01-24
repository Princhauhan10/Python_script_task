'''import boto3
import time

def create_asg():
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '#######'
    secret_key = '######'
    region = 'us-east-1'

    # Connect to AWS
    autoscaling_client = boto3.client('autoscaling', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Specify Auto Scaling Group details
    asg_name = 'my-auto-scaling-group'
    launch_config_name = 'my-launch-con'
    min_size = 1
    max_size = 3
    desired_capacity = 2
    subnet_ids = ['subnet-#########', 'subnet-############']  # Replace with your subnet IDs

    # Create Launch Configuration
    response_lc = autoscaling_client.create_launch_configuration(
        LaunchConfigurationName=launch_config_name,
        ImageId='ami-#################',  # Replace with your AMI ID
        InstanceType='t2.micro',
        KeyName='###',  # Replace with your key pair name
    )

    # Create Auto Scaling Group
    response_asg = autoscaling_client.create_auto_scaling_group(
        AutoScalingGroupName=asg_name,
        LaunchConfigurationName=launch_config_name,
        MinSize=min_size,
        MaxSize=max_size,
        DesiredCapacity=desired_capacity,
        VPCZoneIdentifier=','.join(subnet_ids),
    )

    print(f"Auto Scaling Group {asg_name} created.")

    return asg_name, region, access_key, secret_key

def describe_asg(asg_name, region, access_key, secret_key):
    # Describe Auto Scaling Group details
    autoscaling_client = boto3.client('autoscaling', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = autoscaling_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])

    # Print Auto Scaling Group details
    print("Auto Scaling Group Details:")
    for group in response['AutoScalingGroups']:
        print(f"Auto Scaling Group Name: {group['AutoScalingGroupName']}")
        print(f"Launch Configuration Name: {group['LaunchConfigurationName']}")
        print(f"Min Size: {group['MinSize']}")
        print(f"Max Size: {group['MaxSize']}")
        print(f"Desired Capacity: {group['DesiredCapacity']}")
        print(f"VPC Zone Identifier: {group['VPCZoneIdentifier']}")
        print("Instances:")
        for instance in group['Instances']:
            print(f"  - {instance['InstanceId']}")

def delete_asg(asg_name, region, access_key, secret_key):
    # Delete Auto Scaling Group
    autoscaling_client = boto3.client('autoscaling', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = autoscaling_client.delete_auto_scaling_group(AutoScalingGroupName=asg_name, ForceDelete=True)

    print(f"Auto Scaling Group {asg_name} deleted.")

if __name__ == "__main__":
    asg_name, region, access_key, secret_key = create_asg()

    # Wait for Auto Scaling Group to become active
    time.sleep(60)

    # Describe Auto Scaling Group details
    describe_asg(asg_name, region, access_key, secret_key)

    # Delete Auto Scaling Group
    delete_asg(asg_name, region, access_key, secret_key)
'''

import boto3
import time

def create_launch_configuration(autoscaling_client):
    # Specify Launch Configuration details
    launch_config_name = 'my-launch-con'
    image_id = '###'  # Replace with your AMI ID
    instance_type = '###'
    key_name = '###'  # Replace with your key pair name

    # Create Launch Configuration
    response_lc = autoscaling_client.create_launch_configuration(
        LaunchConfigurationName=launch_config_name,
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
    )

    print(f"Launch Configuration {launch_config_name} created.")

    return launch_config_name

def create_asg(autoscaling_client, launch_config_name, min_size, max_size, desired_capacity, subnet_ids):
    # Create Auto Scaling Group
    asg_name = f'my-auto-scaling-group-{time.time()}'  # Generating a unique name
    response_asg = autoscaling_client.create_auto_scaling_group(
        AutoScalingGroupName=asg_name,
        LaunchConfigurationName=launch_config_name,
        MinSize=min_size,
        MaxSize=max_size,
        DesiredCapacity=desired_capacity,
        VPCZoneIdentifier=','.join(subnet_ids),
    )

    print(f"Auto Scaling Group {asg_name} created.")
    return asg_name

def list_asg_names(autoscaling_client):
    # List only Auto Scaling Group names
    asg_details = autoscaling_client.describe_auto_scaling_groups()
    asg_names = [asg['AutoScalingGroupName'] for asg in asg_details['AutoScalingGroups']]
    return asg_names

def describe_asg(autoscaling_client, asg_name):
    # Describe Auto Scaling Group details
    response = autoscaling_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])

    # Print Auto Scaling Group details
    print("\nAuto Scaling Group Details:")
    for group in response['AutoScalingGroups']:
        print(f"Auto Scaling Group Name: {group['AutoScalingGroupName']}")
        print(f"Launch Configuration Name: {group['LaunchConfigurationName']}")
        print(f"Min Size: {group['MinSize']}")
        print(f"Max Size: {group['MaxSize']}")
        print(f"Desired Capacity: {group['DesiredCapacity']}")
        print(f"VPC Zone Identifier: {group['VPCZoneIdentifier']}")
        print("Instances:")
        for instance in group['Instances']:
            print(f"  - {instance['InstanceId']}")

def delete_asg(autoscaling_client, asg_name):
    # Delete Auto Scaling Group
    response = autoscaling_client.delete_auto_scaling_group(AutoScalingGroupName=asg_name, ForceDelete=True)

    print(f"Auto Scaling Group {asg_name} deleted.")

if __name__ == "__main__":
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    access_key = '######'
    secret_key = '########'
    region = 'us-east-2'

    autoscaling_client = boto3.client('autoscaling', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    # Create Launch Configuration
    launch_config_name = create_launch_configuration(autoscaling_client)

    while True:
        # Create multiple Auto Scaling Groups
        min_size = 1
        max_size = 3
        desired_capacity = 2
        subnet_ids = ['subnet-###########', 'subnet-############S']  # Replace with your subnet IDs

        asg_name = create_asg(autoscaling_client, launch_config_name, min_size, max_size, desired_capacity, subnet_ids)

        # List Auto Scaling Group names
        asg_names = list_asg_names(autoscaling_client)
        print("\nList of Auto Scaling Group Names:")
        for name in asg_names:
            print(name)

        # Choose an Auto Scaling Group to get details
        asg_name_to_get_details = input("\nEnter the Auto Scaling Group Name to get details (or press Enter to skip): ").strip()
        if asg_name_to_get_details:
            describe_asg(autoscaling_client, asg_name_to_get_details)

        # Choose an Auto Scaling Group to delete
        delete_option = input("\nDo you want to delete an Auto Scaling Group? (yes/no): ").strip().lower()
        if delete_option == 'yes':
            asg_name_to_delete = input("Enter the Auto Scaling Group Name to delete: ").strip()
            delete_asg(autoscaling_client, asg_name_to_delete)

        exit_option = input("\nDo you want to exit the loop? (yes/no): ").strip().lower()
        if exit_option == 'yes' or not asg_names:
            break

