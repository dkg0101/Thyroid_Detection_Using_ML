from src.logger import logging
from src.exception import CustomException
import os,sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.constants import *
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts',"train.csv")
    test_data_path:str =os.path.join('artifacts','test.csv')
    raw_data_path:str =os.path.join('artifacts','raw_data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            data_ingestion_config = self.ingestion_config

            df = pd.read_csv('F:\\MachineLearningProject\\Thyroid_Detection_Using_ML\\thyroid0387.data')
            logging.info(' data reading done,cleaning the data...')

            
            df["outcome"] = df["-[840801013]"].str[0]
            df.drop(columns="-[840801013]", inplace=True)
            logging.info('Created outcome column')

            logging.info("Renaming columns with proper column names")

            df.rename(columns=COLUMNS,inplace=True)

            logging.info("Converting oucome column into binary format..")
            df['outcome'].replace(to_replace=OUTCOME_LIST, value="yes", inplace=True)
            df['outcome'].replace({'yes':1,'-':0},inplace=True)

            logging.info("dropping unnecessary features with high missing values")

            df.replace('?', np.nan,inplace=True)
            df.drop(['TBG_measured','TBG','T3_measured','TSH_measured','TT4_measured','T4U_measured','FTI_measured'],axis=1,inplace=True)

            logging.info(f"dataset cleaning done,shape of obtained dataframe is: [{df.shape}] ")



            logging.info(f"saving dataset into artifact folder: [{os.path.dirname(data_ingestion_config.raw_data_path)}]")

            os.makedirs(os.path.dirname(data_ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(data_ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_df,test_df = train_test_split(df,test_size=0.2,random_state=19)

            train_df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion completed ")

            return(
                  data_ingestion_config.train_data_path,
                  data_ingestion_config.test_data_path
                  )
        except Exception as e:
            raise CustomException(e,sys) from e


if __name__=="__main__":
    obj =DataIngestion()
    train_data,test_data= obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    # train_arr,test_arr,_ =data_transformation.initiate_data_transformation(train_data,test_data)


    # modeltrainer = ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


    

