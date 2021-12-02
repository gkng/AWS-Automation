import boto3
import json
client = boto3.client('ec2', region_name='ap-southeast-1')
vpcdata=client.create_vpc(CidrBlock='192.168.0.0/24')
print (type(vpcdata))

print (json.dumps(vpcdata, indent=4))
