import os
import joblib
import numpy as np

def predict(array):
    label_value_mapping={"No_Machine_Failure":"No",
                         "Machine_Failure":"Yes"}
    cwd=os.getcwd()

    transform_pth=os.path.join(cwd,"app","transform.pkl")
    transform=joblib.load(transform_pth)

    encoder_pth=os.path.join(cwd,"app","encoder.pkl")
    encoder=joblib.load(encoder_pth)

    scaled_array=transform.transform(array)

    model_pth=os.path.join(cwd,"app","model.pkl")
    trained_model=joblib.load(model_pth)

    idx=trained_model.predict(scaled_array)[0].item()
    label=encoder.inverse_transform([idx]).item()
    confidence=np.max(trained_model.predict_proba(scaled_array)).item()

    return {"Downtime":label_value_mapping[label],
            "Confidence":confidence}
