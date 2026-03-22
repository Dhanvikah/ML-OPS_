from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def run_pipeline(self):
        # Step 1: Ingestion
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()

        # Step 2: Transformation
        transformation = DataTransformation()
        X_train, X_test, y_train, y_test = transformation.initiate_data_transformation(
            train_path, test_path
        )


        # Step 3: Model Training
        trainer = ModelTrainer()
        best_model_name, best_score = trainer.initiate_model_training(
            X_train, y_train, X_test, y_test
        )

        print("Best Model:", best_model_name)
        print("Best Score:", best_score)