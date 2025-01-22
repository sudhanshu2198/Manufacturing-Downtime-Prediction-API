import shutil
import glob

import numpy as np
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel,Field

from modelling import train
from inference import predict

class Item(BaseModel):
    Torque:float=Field(gt=0)
    Hydraulic_Pressure:float=Field(gt=0)
    Cutting:float=Field(gt=0)
    Coolant_Pressure:float=Field(gt=0)
    Spindle_Speed:float=Field(gt=0)
    Coolant_Temperature:float=Field(gt=0)

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Hello World!"}

@app.post("/upload/")
def upload_csv(uploaded_file:UploadFile=File(...)):
    path="dataset.csv"
    with open(path, 'w+b') as file:
        shutil.copyfileobj(uploaded_file.file, file)

    return {'file': uploaded_file.filename,
            'content': uploaded_file.content_type,
            'path': path}

@app.post("/train/")
def training():
    csv_files=glob.glob("*.csv")
    if "dataset.csv" in csv_files:
        results=train("dataset.csv")
        return results
    else:
        return {"message":"Please upload Dataset"}

@app.post("/predict/")
def prediction(item:Item):
    arr=[[item.Torque,item.Hydraulic_Pressure,item.Cutting,item.Coolant_Pressure,item.Spindle_Speed,item.Coolant_Temperature]]
    results=predict(arr)
    return results










