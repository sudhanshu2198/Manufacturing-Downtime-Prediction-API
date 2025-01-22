import joblib
import numpy as np

def predict(array):
    label_idx_mapping={0:"No",
                       1:"Yes"}
    trained_model=joblib.load("model.pkl")

    idx=trained_model.predict(array)[0].item()
    confidence=np.max(trained_model.predict_proba(array)).item()

    return {"Downtime":label_idx_mapping[idx],
            "Confidence":confidence}
