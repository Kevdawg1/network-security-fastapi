import os
import sys
from datetime import datetime
from networksecurity.logging.logger import logging
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.constants import training_pipeline

class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        try:
            timestamp = timestamp.strftime("%Y%m%d%H%M%S")
            self.timestamp:str =timestamp
            self.pipeline_name = training_pipeline.PIPELINE_NAME
            self.artifact_name = training_pipeline.ARTIFACT_DIR
            self.artifact_dir = os.path.join(self.artifact_name, timestamp)
            self.model_dir = os.path.join("final_models")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
            self.feature_store_file_path = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME)
            
            self.train_test_split_ratio:float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
            self.collection_name:str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
            self.database_name:str = training_pipeline.DATA_INGESTION_DATABASE_NAME
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
            
            self.valid_data_dir = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
            self.invalid_data_dir = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)
            
            self.valid_train_data_file_path = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)
            self.invalid_train_data_file_path = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME)
            
            self.valid_test_data_file_path = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)
            self.invalid_test_data_file_path = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME)
            
            self.drift_report_file_path = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
            self.transformed_train_file_path = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, 
                                                            training_pipeline.DATA_TRANSFORMATION_TRAIN_FILE_PATH)
            self.transformed_test_file_path = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, 
                                                           training_pipeline.DATA_TRANSFORMATION_TEST_FILE_PATH)
            self.transformed_object_file_path = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                             training_pipeline.PREPROCESSING_OBJECT_FILE_NAME)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
class ModelTrainerConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            self.model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME)
            self.trained_model_file_path = os.path.join(self.model_trainer_dir, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,
                                                        training_pipeline.MODEL_TRAINER_TRAINED_MODEL_NAME)
            self.expected_accuracy = training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
            self.overfitting_threshold = training_pipeline.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD
        except Exception as e:
            raise NetworkSecurityException(e, sys)
            