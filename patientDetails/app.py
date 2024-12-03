import boto3

def get_image_set_details(data_store_id, image_set_id):
    client = boto3.client('medical-imaging')

    # Get details of the image set
    response = client.get_image_set(datastoreId=data_store_id, imageSetId=image_set_id)
    
    return response

# Example usage
data_store_id = '21b75fc2d1b640979a3d133ba28bcf27'  # Your datastore ID
image_set_id = '0e989dfc50a3e46f144285e5f5374227'  # Your image set ID

image_set_details = get_image_set_details(data_store_id, image_set_id)

# Extract Series Instance UID
series_instance_uid = image_set_details['seriesInstanceUid'] if 'seriesInstanceUid' in image_set_details else "Unknown"
print(f"Series Instance UID: {series_instance_uid}")