from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import (DataIngestionArtifact)

import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_dataframe(self):
        """
        This function reads the data from MongoDB and exports it as a pandas DataFrame.
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            
            logging.info("Connecting to MongoDB")
            mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            mongo_db = mongo_client[database_name]
            collection = mongo_db[collection_name]
            
            logging.info(f"Exporting collection {collection_name} from MongoDB database {database_name}")
            df = pd.DataFrame(list(collection.find()))
            
            ## Drop the _id column
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
                
            ## Replace na values
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_data_into_feature_store(self, df: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            
            ## Create folder for feature store
            feature_store_dir = os.path.dirname(feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)
            logging.info(f"Feature store directory: {feature_store_dir}")
            
            ## Export as csv
            df.to_csv(feature_store_file_path, index=False, header=True)
            logging.info(f"Feature store csv data exported to {feature_store_file_path}")
            return df
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def split_data_as_train_test(self, df: pd.DataFrame): 
        train, test = train_test_split(df, test_size=self.data_ingestion_config.train_test_split_ratio)
        logging.info(f"Splitting the data into train and test. Train data: {train.shape}. Test data: {test.shape}")
        
        dir_path = os.path.dirname(self.data_ingestion_config.train_file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        logging.info(f"Exporting train and test data into directory: {dir_path}")
        train.to_csv(self.data_ingestion_config.train_file_path, index=False, header=True)
        test.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
        logging.info(f"Train and test data exported to {self.data_ingestion_config.train_file_path} and {self.data_ingestion_config.test_file_path}")
        
        
        return train, test
        
    def initiate_data_ingestion(self):
        try:
            df = self.export_collection_as_dataframe()
            df = self.export_data_into_feature_store(df)
            self.split_data_as_train_test(df)
            
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
