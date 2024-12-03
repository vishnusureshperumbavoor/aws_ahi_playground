import boto3
s3 = boto3.resource('s3')

print('----------------')
print('S3 Buckets')
print('----------------')
for bucket in s3.buckets.all():
    print(bucket.name)