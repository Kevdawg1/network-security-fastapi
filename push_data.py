import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging import logger

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_into_mongodb(self, records, database, collection):
        try: 
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database  = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "network_data/phisingData.csv"
    DATABASE = "NetworkSecurity"
    COLLECTION = "NetworkData"
    try:
        logger.logging.info("Extracting data from csv")
        obj = NetworkDataExtract()
        records = obj.csv_to_json_converter(FILE_PATH)
        logger.logging.info("Pushing data into mongodb")
        no_of_records = obj.insert_data_into_mongodb(records, DATABASE, COLLECTION)
        logger.logging.info(f"Inserted {no_of_records} records into mongodb")
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)