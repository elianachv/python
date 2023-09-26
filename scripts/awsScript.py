#!/bin/python3

"""
Script to list EC2 instances and S3 buckets
Author: Eliana Chavez
"""

import boto3

print("EC2 instances")
client = boto3.client("ec2")
ec2s = client.describe_instances()
instances = ec2s["Reservations"]

print("Instances:", len(instances))
for instance in instances:

    i = instance["Instances"][0]
    print("ID: ", i["InstanceId"])


print("S3 buckets")
client = boto3.client("s3")
s3s = client.list_buckets()
buckets = s3s["Buckets"]

for b in buckets:
    print(b)

create_bucket = input("Do you want to create a new bucket? [y/n] ")

if create_bucket == "y":

    number_buckets = input("How many buckets do you want to create? ")
    bucket_name = input("Digit principal name of new buckets: ")

    if number_buckets.isdigit():
        for i in range(int(number_buckets)):
            response = client.create_bucket(Bucket=bucket_name+"-"+str(i))
            print(response)
    else:
        print("You do not enter a valid number")
else:
    print("Ok")
