from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Creating a class to validate the request body of api


class request_body(BaseModel):
    hours_studied: float


# Creating the FastAPI instance
app = FastAPI()

# Loading the model for predicting
reg_model = joblib.load('./regression_model.pkl')


@app.post('/predict')
def predict(data: request_body):
    # Prepare the data for prediction
    input_feature = [[data.hours_studied]]

    # Realizing the prediction
    y_pred = reg_model.predict(input_feature)[0].astype(int)

    return {'test_score': y_pred.tolist()}

# To run the api run the following command on cmd:
# uvicorn api_regression_model:app --reload
