from fastapi import FastAPI, HTTPException
from app.schemas.prediction import PredictionInput
from app.services.predictor import make_prediction

app = FastAPI()


@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        prediction = make_prediction(input_data.dict())
        return {"predicted_price": round(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
