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

    def get_image_set_metadata(
        self, metadata_file, datastore_id, image_set_id, version_id=None
    ):
        """
        Get the metadata of an image set.

        :param metadata_file: The file to store the JSON gzipped metadata.
        :param datastore_id: The ID of the data store.
        :param image_set_id: The ID of the image set.
        :param version_id: The version of the image set.
        """
        try:
            if version_id:
                image_set_metadata = self.health_imaging_client.get_image_set_metadata(
                    imageSetId=image_set_id,
                    datastoreId=datastore_id,
                    versionId=version_id,
                )
            else:
                image_set_metadata = self.health_imaging_client.get_image_set_metadata(
                    imageSetId=image_set_id,
                    datastoreId=datastore_id
                )

            # Print the retrieved metadata
            print("Retrieved Image Set Metadata:")
            print(image_set_metadata)

            # Extract and print patient details
            patient_details = image_set_metadata.get("patient", {})
            if patient_details:
                print("\nPatient Details:")
                print(f"Patient Name: {patient_details.get('name', 'N/A')}")
                print(f"Patient ID: {patient_details.get('id', 'N/A')}")
                print(f"Patient Birth Date: {patient_details.get('birthDate', 'N/A')}")
                print(f"Patient Sex: {patient_details.get('sex', 'N/A')}")
            else:
                print("No patient details found.")

            # Write the metadata to a file
            with open(metadata_file, "wb") as f:
                for chunk in image_set_metadata["imageSetMetadataBlob"].iter_chunks():
                    if chunk:
                        f.write(chunk)

        except ClientError as err:
            logger.error(
                "Couldn't get image metadata. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

# Create Boto3 client and wrapper instance
client = boto3.client("medical-imaging")
medical_imaging_wrapper = MedicalImagingWrapper(client)

# Example usage
version_id = None  # Optional; specify if needed
metadata_file = 'image_set_metadata.json.gz'  # Desired output file name

try:
    medical_imaging_wrapper.get_image_set_metadata(metadata_file, DATASTORE_ID, IMAGE_SET_ID, version_id)
except Exception as e:
    logger.error("An error occurred: %s", e)