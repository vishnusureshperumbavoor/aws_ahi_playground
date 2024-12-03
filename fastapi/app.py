import boto3
from fastapi import FastAPI, HTTPException
from botocore.exceptions import ClientError
from pydantic import BaseModel

app = FastAPI()

# Create a Boto3 client for Medical Imaging
client = boto3.client('medical-imaging', region_name='us-east-1')

# Define a model for the request body (if needed)
class DatastoreRequest(BaseModel):
    # You can add fields here if you want to accept parameters
    # For example: filter: str = None
    pass  # Currently no parameters are needed

@app.post("/datastores/")
async def list_datastores(datastore_request: DatastoreRequest):
    try:
        # Call the list_datastores method
        response = client.list_datastores()
        datastores = response.get('datastoreSummaries', [])
        print(datastores)

        # Return the list of data stores
        return [
            {
                "datastoreId": ds['datastoreId'],
                "datastoreName": ds['datastoreName'],
                "status": ds['datastoreStatus']
            } for ds in datastores
        ]

    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)