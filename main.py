from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig, TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig, DataTransformationConfig

from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys

if __name__ == "__main__":
    try:
        logging.info("Initialise Data Ingestion Configurations")
        training_pipe_line_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipe_line_config)
        logging.info("Initiate Data Ingestion Pipeline")
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        
        logging.info("Initiate Data Validation Configurations")
        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipe_line_config)
        logging.info("Initiate Data Validation Pipeline")
        data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, 
                                         data_validation_config=data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        
        logging.info("Initiate Data Transformation Configurations")
        data_transformation_config = DataTransformationConfig(training_pipeline_config=training_pipe_line_config)
        logging.info("Initiate Data Transformation Pipeline")
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact, 
                                                 data_transformation_config=data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        
        logging.info("Initiate Model Training Configurations")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config=training_pipe_line_config)
        logging.info("Initiate Model Training Pipeline")
        model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact, 
                                                 model_trainer_config=model_trainer_config)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training Completed")
    except Exception as e:
        raise NetworkSecurityException(e, sys)