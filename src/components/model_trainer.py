import os
import sys
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomException


class ModelTrainer:
    def __init__(self):
        self.model_path = "artifacts/model.pkl"

    def evaluate_model(self, X_train, y_train, X_test, y_test, models):
        try:
            report = {}

            for name, model in models.items():
                logging.info(f"Training model: {name}")

                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                score = r2_score(y_test, y_pred)

                report[name] = score

                logging.info(f"{name} R2 Score: {score}")

            return report

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_training(self, X_train, y_train, X_test, y_test):
        try:
            logging.info("Model Training Started")

            models = {
                "LinearRegression": LinearRegression(),
                "DecisionTree": DecisionTreeRegressor(),
                "RandomForest": RandomForestRegressor()
            }

            model_report = self.evaluate_model(
                X_train, y_train, X_test, y_test, models
            )

            # Select best model
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]

            best_model = models[best_model_name]

            logging.info(f"Best Model: {best_model_name} with score {best_model_score}")

            # Save best model
            os.makedirs("artifacts", exist_ok=True)
            with open(self.model_path, "wb") as f:
                pickle.dump(best_model, f)

            logging.info("Best model saved")

            return best_model_name, best_model_score

        except Exception as e:
            raise CustomException(e, sys)