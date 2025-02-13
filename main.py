from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig

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
    except Exception as e:
        raise NetworkSecurityException(e, sys)