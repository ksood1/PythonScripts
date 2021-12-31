import sys
import boto3
import csv


def get_cidr(ak_id,sa_key):
    client = boto3.client('ec2',region_name='us-east-1',aws_access_key_id=ak_id,aws_secret_access_key=sa_key)
    response = client.describe_vpcs()

    resp = response['Vpcs']

    #print(resp)
    
    for val in resp:
        
        if 'CidrBlock' in val and 'VpcId' in val:
            cdr_blk = (val['CidrBlock'])
            vpcid = (val['VpcId'])
            print('VPC ID: ' + vpcid + ' CidrBlk: '+ cdr_blk)






def auth(input_file):

    with open (input_file,"r") as var_read:
        var_line = csv.reader(var_read,delimiter=",")

        for lines in var_line:

            aws_access_key_id = lines[0]
            aws_secret_access_key = lines[1]
    get_cidr(aws_access_key_id,aws_secret_access_key)



auth(r'd:\AWS\Python Scripts\profile.txt')

