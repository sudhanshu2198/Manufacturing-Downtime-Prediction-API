# Manufacturing Downtime Prediction

## Project Links: 
* **[Deployed FastAPI](https://omdena-jakarta-traffic-system.streamlit.app/)**
* **[Detailed Kaggle Notebook](https://www.kaggle.com/code/sudhanshu2198/machine-defect-prediction)**

## Background
- The Manufacturing Downtime Dataset contains information about the operational parameters of various machines and their downtime records.
- Analyze machine performance, predict potential failures, and develop predictive maintenance strategies based on operational parameters.
- Features
  - Torque(Nm)
  - Hydraulic_Pressure(bar)
  - Cutting(kN)
  - Coolant_Pressure(bar)
  - Spindle_Speed(RPM)
  - Coolant_Temperature
- Target
  - Downtime
 
## Plots

RandomForest Model is using for modelling the relation between features and target variable in Manufacturing Downtime Dataset.

- Accuracy: **0.9897**
- F1_Score: **0.9896**

#### Feature Correlation
![](https://github.com/sudhanshu2198/Manufacturing-Downtime-Prediction-API/blob/main/plots/Feature_Correlation.jpg)

#### Feature Importance
![](https://github.com/sudhanshu2198/Manufacturing-Downtime-Prediction-API/blob/main/plots/Feature_importance.jpg)

#### Confusion Matrix
![](https://github.com/sudhanshu2198/Manufacturing-Downtime-Prediction-API/blob/main/plots/Confusion_Matrix.jpg)

## 🛠 Skills
Numpy, Pandas, Scikit-learn, FastAPI,  Git

## Directory Tree
```bash

├── app
│   ├── __init__.py
│   ├── main.py
│   ├── modelling.py
│   └──  inference.py
├── README.md
├── requirements.txt
├── Manufacturing_Downtime_Dataset.csv
└── .gitignore
```

## Run Webapp Locally

Clone the project

```bash
  git clone https://github.com/sudhanshu2198/Manufacturing-Downtime-Prediction-API
```

Change to project directory

```bash
  cd Manufacturing-Downtime-Prediction-API
```
Create Virtaul Environment and install dependencies

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

Run Locally
```bash

  uvicorn app.main:app

  ```



cURL Commands
1) Upload
```bash

Request
curl -X 'POST' \
  'http://127.0.0.1:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'uploaded_file=@Manufacturing_Downtime_Dataset.csv;type=text/csv'

Response
{
  "file": "Manufacturing_Downtime_Dataset.csv",
  "content": "text/csv",
  "path": "dataset.csv"
}

```
2) Train
```bash
Request
curl -X 'POST' \
  'http://127.0.0.1:8000/train/' \
  -H 'accept: application/json' \
  -d ''
Response
  {
  "Accuracy": 0.9897750511247444,
  "F1_Score": 0.9896049896049895
  }
```
3) Predict
```bash
Request 1
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Torque": 28.38124,
  "Hydraulic_Pressure": 131.265854,
  "Cutting": 2.01,
  "Coolant_Pressure": 4.982836,
  "Spindle_Speed": 20033.0,
  "Coolant_Temperature": 20.1
}'

Response 1
{
  "Downtime": "No",
  "Confidence": 0.87
}

Request 2
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Torque": 25.614444,
  "Hydraulic_Pressure": 98.7,
  "Cutting": 3.49,
  "Coolant_Pressure": 6.839413,
  "Spindle_Speed": 18638.0,
  "Coolant_Temperature": 24.4
}'

Response 2
{
  "Downtime": "Yes",
  "Confidence": 0.98
}
```

