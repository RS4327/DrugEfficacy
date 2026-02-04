import numpy as np
import pandas as pd
from DrugEfficacy.Config.CongurationManager import ConfigurationManagerConfig
from DrugEfficacy.Components.Data_Feature_Engineering import DataFeatureEnginerring
from DrugEfficacy.Utils.common import *
from DrugEfficacy import logger


Stage_Name = 'Data Feature Engineering'


class DataFeatureEngineeringPipeline:
    def __init__(self):
        #  Load configuration object once
        self.config_manager = ConfigurationManagerConfig()
        self.data_feature_engineering_config = self.config_manager.getdatafeatureengineering()

    def main(self, df: pd.DataFrame):
        try:
            #  Pass config to your component
            data_fe = DataFeatureEnginerring(config=self.data_feature_engineering_config)

            #  Step 1: Create target
            target = data_fe.create_target(df)

            # Step 2: Build feature vectorizer (X, y)
            X, y = data_fe.build_vectorizer(target)

            logger.info(" Feature Engineering completed successfully.")
            return X, y

        except Exception as e:
            logger.exception(f" Error in {Stage_Name} pipeline: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f'<<<<<<<<<<<<<<<<<<<< Stage : {Stage_Name} Started >>>>>>>>>>>>>>>>>>>>>>>')
        
        #  Example: Load your preprocessed data here
        df = pd.read_csv("artifacts/Data_PreProcessing/cleaned_data.csv")

        obj = DataFeatureEngineeringPipeline()
        X, y = obj.main(df)  #  Pass df
        
        logger.info(f'<<<<<<<<<<<<<<<<<<<< Stage : {Stage_Name} Successfully Completed >>>>>>>>>>>>>>>>>>>>>>>')

    except Exception as e:
        logger.exception(e)
        raise e
