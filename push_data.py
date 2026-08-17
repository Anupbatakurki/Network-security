import os
import sys
import json
import certifi

import pandas as pd
import pymongo

from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


# Load environment variables
load_dotenv()

# Get MongoDB connection string
MONGO_DB_URL = os.getenv("MONGODB_URL_KEY")

if not MONGO_DB_URL:
    raise ValueError("MONGODB_URL_KEY is not found in .env")


class NetworkDataExtract:

    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):

        try:
            data = pd.read_csv(file_path)

            data.reset_index(drop=True, inplace=True)

            records = list(
                json.loads(
                    data.T.to_json()
                ).values()
            )

            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(
        self,
        records,
        database,
        collection
    ):

        try:

            self.database = database
            self.collection = collection
            self.records = records

            # Connect to MongoDB Atlas
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=10000
            )

            # Test connection
            self.mongo_client.admin.command("ping")

            print("MongoDB Atlas connection SUCCESS!")

            # Select database
            self.database = self.mongo_client[self.database]

            # Select collection
            self.collection = self.database[self.collection]

            # Insert records
            result = self.collection.insert_many(self.records)

            print(
                f"Successfully inserted "
                f"{len(result.inserted_ids)} records."
            )

            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    FILE_PATH = r"Network_Data\phisingData.csv"

    DATABASE = "Anup"

    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()

    print("Reading dataset...")

    records = networkobj.csv_to_json_convertor(
        file_path=FILE_PATH
    )

    print(
        f"Total records found: {len(records)}"
    )

    no_of_records = networkobj.insert_data_mongodb(
        records,
        DATABASE,
        COLLECTION
    )

    print(
        f"Total records inserted: {no_of_records}"
    )