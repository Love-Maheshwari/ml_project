#A Data Ingestion component is responsible for gathering raw data from various sources (databases, APIs, files, etc.), processing it, 
# and storing it for further use in a data pipeline. This is the first step in any ETL (Extract, Transform, Load) pipeline or ML pipeline.

import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class variables

# there are some input to be the in data ingestion like where to train data, test data and save raw data etc...
# so therse will be in DataIngestionConfig

@dataclass    # to directly define your class variables
class DataIngestionConfig:
    # Create a path for train.csv inside the "artifact" directory
    # these are some input to data ingestion component that will be stored at specified path
    train_data_path: str=os.path.join('artifact', "train.csv")
    test_data_path: str=os.path.join('artifact',"test.csv")
    raw_data_path: str=os.path.join('artifact',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #this will initialize the above three variables in ingestion_config    

    def intiate_data_ingestion(self):
        logging.info("entered the data ingestion component")
        #we will use try and except for exception handling like if data csv or path not found etc
        try:
            #here we can read-csv or from any database or APi's
            df = pd.read_csv('Project_2/Notebooks/data/stud.csv')
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("data Ingestion completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__== "__main__":
    obj=DataIngestion()
    obj.intiate_data_ingestion()