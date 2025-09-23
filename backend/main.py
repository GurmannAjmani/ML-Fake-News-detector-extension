from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from test_preprocessor import test_preprocessor
from fastapi.middleware.cors import CORSMiddleware

# Load model + label encoder at startup
rf = joblib.load("random_forest_model.joblib")
le = joblib.load("label_encoder.joblib")

app = FastAPI()

class InputText(BaseModel):
    text: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "API is running. Use POST /predict"}
@app.post("/predict")
def predict_news(data: InputText):
    processed = test_preprocessor(data.text)
    prediction = rf.predict(processed)
    label = le.inverse_transform(prediction)[0]
    return {"result": label}