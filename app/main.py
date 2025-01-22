import shutil
import glob
import os

import numpy as np
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel,Field

from app.modelling import train
from app.inference import predict

class Item(BaseModel):
    Torque:float=Field(gt=0,default=24.25)
    Hydraulic_Pressure:float=Field(gt=0,default=121.86)
    Cutting:float=Field(gt=0,default=2.89)
    Coolant_Pressure:float=Field(gt=0,default=6.96)
    Spindle_Speed:float=Field(gt=0,default=20504.0)
    Coolant_Temperature:float=Field(gt=0,default=14.9)

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Hello World!"}

@app.post("/upload/")
def upload_csv(uploaded_file:UploadFile=File(...)):
    cwd=os.getcwd()
    path=os.path.join(cwd,"app","dataset.csv")
    with open(path, 'w+b') as file:
        shutil.copyfileobj(uploaded_file.file, file)

    return {'file': uploaded_file.filename,
            'content': uploaded_file.content_type,
            'path': path}

@app.post("/train/")
def training():
    cwd=os.getcwd()
    path=os.path.join(cwd,"app","dataset.csv")
    if os.path.exists(path):
        results=train(path)
        return results
    else:
        return {"message":"First Upload Dataset"}

@app.post("/predict/")
def prediction(item:Item):
    cwd=os.getcwd()
    path=os.path.join(cwd,"app","model.pkl")
    if os.path.exists(path):
        arr=[[item.Torque,item.Hydraulic_Pressure,item.Cutting,item.Coolant_Pressure,item.Spindle_Speed,item.Coolant_Temperature]]
        results=predict(arr)
        return results
    else:
        return {"message":"First Train Model"}










