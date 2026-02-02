import pandas as pd
from pathlib import Path
from DrugEfficacy import logger
from DrugEfficacy.Entity.Entity_Config import *
from DrugEfficacy.Utils.common import *


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

        create_directories([self.config.root_dir])
    def DataLoading(self):
        csv_path=self.config.source_path
        df=pd.read_csv(csv_path)
        logger.info(f'Data Frame shape :{df.shape}')
        logger.info(f"Data Frame Information :{df.info()}")
        logger.info(f"Data Frame :{df.head(2)}")
        logger.info(f'unique values for Drug Name :\n{df['condition'].nunique()}')
        condition_counts = df['condition'].value_counts()
        logger.info(f" Count of records for group by condition : {condition_counts}")
        return df

