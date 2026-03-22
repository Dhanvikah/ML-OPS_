import os
import sys
import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

from src.logger import logging
from src.exception import CustomException


class DataTransformation:
    def __init__(self):
        self.preprocessor_path = "artifacts/preprocessor.pkl"

    def get_data_transformer(self, df):
        try:
            logging.info("Auto-detecting column types")

            # Separate numerical & categorical automatically
            numerical_columns = ["Gr Liv Area", "Bedroom AbvGr", "Full Bath"]
            categorical_columns = ["Neighborhood"]

            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            # Remove target column if present
            if "SalePrice" in numerical_columns:
                numerical_columns.remove("SalePrice")

            # Numerical pipeline
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            # Categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
            ])

            preprocessor = ColumnTransformer([
                ("num", num_pipeline, numerical_columns),
                ("cat", cat_pipeline, categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data Transformation started")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            # ✅ Select only important columns
            selected_columns = ["Gr Liv Area", "Bedroom AbvGr", "Full Bath", "Neighborhood", "SalePrice"]

            train_df = train_df[selected_columns]
            test_df = test_df[selected_columns]
            target_column = "SalePrice"

            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]

            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            preprocessor = self.get_data_transformer(train_df)

            logging.info("Fitting preprocessor")

            X_train_transformed = preprocessor.fit_transform(X_train)
            X_test_transformed = preprocessor.transform(X_test)

            # Save preprocessor
            os.makedirs("artifacts", exist_ok=True)
            with open(self.preprocessor_path, "wb") as f:
                pickle.dump(preprocessor, f)

            logging.info("Preprocessor saved")

            return (
                X_train_transformed,
                X_test_transformed,
                y_train,
                y_test
            )

        except Exception as e:
            raise CustomException(e, sys)