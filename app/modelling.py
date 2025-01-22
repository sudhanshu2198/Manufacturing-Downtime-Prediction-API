import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PowerTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import argparse
import joblib

def train(dataset_pth):
        df=pd.read_csv(dataset_pth)
        features=["Torque(Nm)","Hydraulic_Pressure(bar)","Cutting(kN)","Coolant_Pressure(bar)","Spindle_Speed(RPM)","Coolant_Temperature","Downtime"]

        df=df[features]
        df.dropna(inplace=True,ignore_index=True)
        X=df.drop("Downtime",axis=1)
        y=df["Downtime"]

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42,stratify=y)

        transform=PowerTransformer()
        X_train=transform.fit_transform(X_train)
        X_test=transform.transform(X_test)

        encoder=LabelEncoder()
        y_train=encoder.fit_transform(y_train)
        y_test=encoder.transform(y_test)

        model=RandomForestClassifier(random_state=42)
        model.fit(X_train,y_train)
        predict=model.predict(X_test)

        cwd=os.getcwd()
        transform_pth=os.path.join(cwd,"app","transform.pkl")
        encoder_pth=os.path.join(cwd,"app","encoder.pkl")
        model_pth=os.path.join(cwd,"app","model.pkl")

        joblib.dump(transform,transform_pth)
        joblib.dump(encoder,encoder_pth)
        joblib.dump(model,model_pth)

        return {"Accuracy":accuracy_score(y_test,predict),
                "F1_Score":f1_score(y_test,predict)}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--dataset_pth",default="/home/sudhanshu/manufacturing_defect/Manufacturing_Downtime_Dataset.csv")
    args=parser.parse_args()
    results=train(args.dataset_pth)

    print(f"Accuracy: {results['Accuracy']}\n")
    print(f"F1_Score: {results['F1_Score']}")






