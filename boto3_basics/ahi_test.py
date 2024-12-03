import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

print('-'*40)
print('AHI Data Stores')
print('-'*40)

def list_datastores():
    client = boto3.client('medical-imaging')

    try:
        response = client.list_datastores()
        datastores = response.get('datastoreSummaries', [])

        for datastore in datastores:
            print(f"Data Store ID: {datastore['datastoreId']}")
            print(f"Data Store Name: {datastore['datastoreName']}")
            print(f"Data Store Status: {datastore['datastoreStatus']}")
            print(f"Data Store ARN: {datastore['datastoreArn']}")
            print(f"Created At: {datastore['createdAt']}")
            print(f"Updated At: {datastore['updatedAt']}")
            print("-" * 40)

    except ClientError as e:
        print(f"Error fetching data stores: {e.response['Error']['Message']}")

if __name__ == "__main__":
    list_datastores()