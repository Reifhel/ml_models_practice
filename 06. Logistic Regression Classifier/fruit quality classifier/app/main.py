from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib

# Create a fastapi Instance
app = FastAPI()

# Create a class with our request data


class request_body(BaseModel):
    A_id: int
    Size: float
    Weight: float
    Sweetness: float
    Crunchiness: float
    Juiciness: float
    Ripeness: float
    Acidity: float


# Load the model
lr_model = joblib.load('./fruit_quality_model.pkl')


@app.post('/classify')
def predict(data: request_body):
    # Prepare the features
    input_features = [[data.Size, data.Weight, data.Sweetness,
                       data.Crunchiness, data.Juiciness, data.Ripeness, data.Acidity]]

    # Classify the fruit
    y_pred = lr_model.predict(input_features)[0].astype(int)
    y_prob = lr_model.predict_proba(input_features)[0].astype(float)

    response = "Good" if y_pred == 1 else "Bad"
    prob = y_prob[y_pred] * 100

    return {"Quality": response, "Probability": prob}
