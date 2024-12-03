import boto3
import io
import pydicom

def get_patient_details(bucket_name, object_key):
    s3_client = boto3.client('s3')
    
    # Get the object
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    
    # Read DICOM from memory
    dicom_file = pydicom.dcmread(io.BytesIO(response['Body'].read()))
    
    # Print patient details
    print("Patient Name:", dicom_file.PatientName)
    print("Patient ID:", dicom_file.PatientID)
    print("Patient Birth Date:", dicom_file.PatientBirthDate)
    print("Patient Sex:", dicom_file.PatientSex)

# Example usage
bucket_name = 'dicombucketvsp'
object_key = 'dicom_files/test_dicom.DCM'
get_patient_details(bucket_name, object_key)