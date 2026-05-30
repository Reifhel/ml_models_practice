from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Create a instance from FastAPI
app = FastAPI()

# Creating a class with the input data from the request body


class request_body(BaseModel):
    months_with_the_company: int
    job_level: int


# Loading the model to make a prediction
polynomial_model = joblib.load('./salary_forecast_model.pkl')


# Function to make the prediction
@app.post('/predict')
def predict(data: request_body):

    input_features = {
        'months_with_the_company': data.months_with_the_company,
        'job_level': data.job_level
    }

    pred_df = pd.DataFrame(input_features, index=[1])

    y_pred = polynomial_model.predict(pred_df)[0].astype(float)

    return {'salary_in_reais': y_pred.tolist()}
