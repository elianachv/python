#!/bin/python3

import boto3

print("EC2 instances")
client = boto3.client("ec2")
ec2s = client.describe_instances()
instances = ec2s["Reservations"]

print("Instances:",len(instances))
for instance in instances:

    i = instance["Instances"][0]
    print("ID: ", i["InstanceId"])


print("S3 buckets")
client = boto3.client("s3")
s3s = client.list_buckets()
buckets = s3s["Buckets"]

for b in buckets:
    print(b)

create_bucket = input("Do you want to create a new bucket? [y/n]")

if create_bucket == "y":
    
    bucket_name = input("Digit name of new bucket: ")
    response = client.create_bucket(Bucket=bucket_name)
    
    print(response)
else:

    print("Ok")
