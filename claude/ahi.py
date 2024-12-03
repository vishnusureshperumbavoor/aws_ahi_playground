import awsHealthImaging as ahi

def get_patient_details(imageset_id):
    imaging_client = ahi.client('medical-imaging')
    
    # Retrieve the imageset
    imageset = imaging_client.get_image_set(imageSetId=imageset_id)
    
    # Extract DICOM metadata
    dicom_metadata = imageset['dicomMetadata']
    
    # Print patient details
    print("Patient Name:", dicom_metadata.get('PatientName'))
    print("Patient ID:", dicom_metadata.get('PatientID'))
    print("Patient Birth Date:", dicom_metadata.get('PatientBirthDate'))
    print("Patient Sex:", dicom_metadata.get('PatientSex'))

# Example usage
imageset_id = 'your-imageset-id'
get_patient_details(imageset_id)