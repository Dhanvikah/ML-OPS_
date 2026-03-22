from fastapi import FastAPI
from pydantic import BaseModel

from src.pipelines.prediction_pipeline import PredictPipeline

app = FastAPI()

# Define input schema (IMPORTANT)
class HouseData(BaseModel):
    Gr_Liv_Area: float
    Bedroom_AbvGr: int
    Full_Bath: int
    Neighborhood: str


@app.get("/")
def home():
    return {"message": "ML Model API Running 🚀"}


@app.post("/predict")
def predict(data: HouseData):
    try:
        input_data = data.dict()

        pipeline = PredictPipeline()
        result = pipeline.predict(input_data)

        return {"prediction": result}

    except Exception as e:
        return {"error": str(e)}

        