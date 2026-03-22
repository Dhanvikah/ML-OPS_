import sys
import pickle
import pandas as pd

from src.exception import CustomException


class PredictPipeline:
    def __init__(self):
        self.model_path = "artifacts/model.pkl"
        self.preprocessor_path = "artifacts/preprocessor.pkl"

    def predict(self, features: dict):
        try:
            # Convert input dict → DataFrame
            df = pd.DataFrame([{
            "Gr Liv Area": features["Gr_Liv_Area"],
            "Bedroom AbvGr": features["Bedroom_AbvGr"],
            "Full Bath": features["Full_Bath"],
            "Neighborhood": features["Neighborhood"]
            }])

            # Load preprocessor
            with open(self.preprocessor_path, "rb") as f:
                preprocessor = pickle.load(f)

            # Transform input
            data_transformed = preprocessor.transform(df)

            # Load model
            with open(self.model_path, "rb") as f:
                model = pickle.load(f)

            # Predict
            prediction = model.predict(data_transformed)

            return prediction[0]

        except Exception as e:
            raise CustomException(e, sys)