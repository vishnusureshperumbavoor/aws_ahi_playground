import boto3
from fastapi import FastAPI, HTTPException
from botocore.exceptions import ClientError
from pydantic import BaseModel

app = FastAPI()
client = boto3.client('medical-imaging', region_name='us-east-1')

class DatastoreRequest(BaseModel):
    pass

@app.post("/datastores/")
async def list_datastores(datastore_request: DatastoreRequest):
    try:
        response = client.list_datastores()
        datastores = response.get('datastoreSummaries', [])
        return datastores

    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)