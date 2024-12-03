import boto3
from botocore.exceptions import ClientError
import logging
from constants import DATASTORE_ID

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client

    def get_datastore_properties(self, datastore_id):
        """
        Get the properties of a data store.

        :param datastore_id: The ID of the data store.
        :return: The data store properties.
        """
        try:
            data_store = self.health_imaging_client.get_datastore(
                datastoreId=datastore_id
            )
        except ClientError as err:
            logger.error(
                "Couldn't get data store %s. Here's why: %s: %s",
                datastore_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return data_store["datastoreProperties"]

# Create Boto3 client and wrapper instance
client = boto3.client("medical-imaging")
medical_imaging_wrapper = MedicalImagingWrapper(client)

try:
    # Get and print the properties of the specified data store
    properties = medical_imaging_wrapper.get_datastore_properties(DATASTORE_ID)
    print("Data Store Properties:")
    for key, value in properties.items():
        print(f"{key}: {value}")
except Exception as e:
    logger.error("An error occurred: %s", e)