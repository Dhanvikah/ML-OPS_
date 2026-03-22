import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException


class DataIngestion:
    def __init__(self):
        self.raw_data_path = "artifacts/raw.csv"
        self.train_path = "artifacts/train.csv"
        self.test_path = "artifacts/test.csv"

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")

        try:
            df = pd.read_csv("data/house_data.csv")

            os.makedirs("artifacts", exist_ok=True)

            # Save raw data
            df.to_csv(self.raw_data_path, index=False)

            logging.info("Raw data saved")

            # Train test split
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42
            )

            train_set.to_csv(self.train_path, index=False)
            test_set.to_csv(self.test_path, index=False)

            logging.info("Train-test split done")

            return self.train_path, self.test_path

        except Exception as e:
            raise CustomException(e, sys)