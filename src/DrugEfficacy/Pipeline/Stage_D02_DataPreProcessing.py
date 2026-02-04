import numpy as np
import pandas as pd
from DrugEfficacy.Config.CongurationManager import ConfigurationManagerConfig
from DrugEfficacy.Components.Data_PreProcessing import DataPreProcessing
from DrugEfficacy import logger

Stage_Name='Data PreProcessing'

class DataPreProcessingPipeline:
    def __init__(self):
        pass

    def main(self,df):
        try:
           
            config=ConfigurationManagerConfig()
            datapreprocessingconfig=config.getdatapreprocessing()
            data_pre=DataPreProcessing(config=datapreprocessingconfig)
            processed_df=data_pre.process(df)
            logger.info(f" Data PreProcessing completed successfully. Shape: {processed_df.shape}")
            return processed_df
        except Exception as e:
            logger.info(f" Error at DataPreProcessing Pipe Line")


if __name__ =='__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} started >>>>>>>>>>>>>>>>>>>>>>")
        obj=DataPreProcessingPipeline()
        obj.main()
        
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} Completed Successfully  >>>>>>>>>>>>>>>>>>>>>>")
    except  Exception as e:
        logger.info(e)
        raise e




