import boto3
from botocore.exceptions import ClientError
import logging
from constants import DATASTORE_ID, IMAGE_SET_ID

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client

    def get_image_set(self, datastore_id, image_set_id, version_id=None):
        try:
            if version_id:
                image_set = self.health_imaging_client.get_image_set(
                    imageSetId=image_set_id,
                    datastoreId=datastore_id,
                    versionId=version_id,
                )
            else:
                image_set = self.health_imaging_client.get_image_set(
                    imageSetId=image_set_id,
                    datastoreId=datastore_id
                )
        except ClientError as err:
            logger.error(
                "Couldn't get image set. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return image_set


# Create Boto3 client and wrapper instance
client = boto3.client("medical-imaging")
medical_imaging_wrapper = MedicalImagingWrapper(client)

version_id = None  # Optional; specify if needed

try:
    # Get and print the properties of the specified image set
    image_set_properties = medical_imaging_wrapper.get_image_set(DATASTORE_ID, IMAGE_SET_ID, version_id)
    
    print('-'*40)
    print("Image Set Properties:")
    print('-'*40)
    for key, value in image_set_properties.items():
        print(f"{key}: {value}")
except Exception as e:
    logger.error("An error occurred: %s", e)