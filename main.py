from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Initialisation"}

@app.get("/datagouv")
async def get_data_from_ademe():
    response = requests.get("https://data.ademe.fr/data-fair/api/v1/datasets/base-carboner/", headers={"accept": "application/json"})
    return response.json()

@app.get("/health_check")
async def health_check():
    return {"status": "API is healthy"}
