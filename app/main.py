from fastapi import FastAPI, HTTPException
import pickle
import numpy as np
import pandas as pd
from House import House

# load model
with open("./model/xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict(features: House):
    try:
        # Get transformed features as a dict
        input_dict = features.transformed_features()
        # Convert to DataFrame with one row
        input_df = pd.DataFrame([input_dict])
        # Ensure categorical columns are formatted as in training
        input_df['Region'] = input_df['Region'].astype(str).str.replace(' ', '_').astype('category')
        input_df['Type'] = input_df['Type'].astype(str).str.replace(' ', '_').astype('category')
        # Predict log price
        log_price_pred = model.predict(input_df)[0]
        # Convert log price back to original price scale
        predicted_price = np.expm1(log_price_pred)
        return {"predicted_price": float(predicted_price)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))