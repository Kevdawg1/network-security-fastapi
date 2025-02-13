import sys, os
import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataTransformationConfig

from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

from networksecurity.logging.logger import logging
from networksecurity.exceptions.exception import NetworkSecurityException

class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact, data_transformation_config: DataTransformationConfig):
        try:
            self.data_transformation_artifact = data_transformation_config
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def get_data_transformer(cls) -> Pipeline:
        try:
            imputer:KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialised KNNImputer with parameters: {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor:Pipeline = Pipeline([('imputer', imputer)])
            return processor
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info('Loading validation dataset')
            train_df = DataTransformation.read_data(file_path=self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(file_path=self.data_validation_artifact.valid_test_file_path)

            X_train = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            y_train = train_df[TARGET_COLUMN]
            y_train = y_train.replace(-1, 0)
            
            X_test = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            y_test = test_df[TARGET_COLUMN]
            y_test = y_test.replace(-1, 0)
            
            preprocessor = self.get_data_transformer()
            
            logging.info("Applying preprocessing object on training and testing datasets")
            preprocessor_obj = preprocessor.fit(X_train)
            X_transformed_train = preprocessor_obj.transform(X_train)
            X_transformed_test = preprocessor_obj.transform(X_test)
            
            train_arr = np.c_[X_transformed_train, y_train]
            test_arr = np.c_[X_transformed_test, y_test]
            
            logging.info("Saving preprocessor object and transformed datasets")
            save_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path, array=train_arr)
            save_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path, array=test_arr)
            save_object(file_path=self.data_transformation_artifact.transformed_object_file_path, obj=preprocessor_obj)
            
            logging.info("Preparing Data Transformation artifact")
            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_artifact.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_artifact.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_artifact.transformed_object_file_path
            )
            
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)