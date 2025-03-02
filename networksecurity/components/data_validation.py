from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig

from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH

from scipy.stats import ks_2samp

import pandas as pd
import os, sys

from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def validate_num_columns(self, df: pd.DataFrame) -> bool:
        try:
            num_columns = len(self._schema_config)
            logging.info(f"Required number of columns: {num_columns}")
            logging.info(f"Dataframe has number of columns: {len(df.columns)}")
            return num_columns == len(df.columns)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def detect_data_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1, d2)
                is_found = False
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    status = False
                    is_found = True
                    logging.warning(f"Column: {column} has drift")
                report.update({column: {
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found
                }})
                
            ## Create Drift Report Directory
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            ## Save the report
            write_yaml_file(drift_report_file_path, content=report)
            
            return status
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_data_validation(self) -> DataValidationArtifact: 
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            ## Read data from train and test
            train_df = DataValidation.read_data(train_file_path)
            test_df = DataValidation.read_data(test_file_path)
            
            ## Validate number of columns
            logging.info("Validating number of columns from train and test data")
            validation_status = self.validate_num_columns(train_df)
            if validation_status != True: 
                error_message = f"Train dataframe does not contain all columns. \n"
            validation_status = self.validate_num_columns(test_df)
            if validation_status != True: 
                error_message = f"Test dataframe does not contain all columns. \n"
            
            ## Check Data Drift
            status = self.detect_data_drift(base_df=train_df, current_df=test_df)
            
            ## Save the report
            dir_path = os.path.dirname(self.data_validation_config.valid_train_data_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_df.to_csv(self.data_validation_config.valid_train_data_file_path, index=False, header=True)
            test_df.to_csv(self.data_validation_config.valid_test_data_file_path, index=False, header=True)
            
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_data_file_path,
                invalid_train_file_path=self.data_validation_config.invalid_train_data_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_data_file_path,
                invalid_test_file_path=self.data_validation_config.invalid_test_data_file_path,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )
            
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)