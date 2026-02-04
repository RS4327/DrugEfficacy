from DrugEfficacy import logger
from DrugEfficacy.Pipeline.Stage_D01_DataIngestoin import DataIngestionPipeline
from DrugEfficacy.Pipeline.Stage_D02_DataPreProcessing import DataPreProcessingPipeline
from DrugEfficacy.Pipeline.Stage_D03_DataFeatureEngineering import DataFeatureEngineeringPipeline
from pathlib import Path
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

Stage_Name='Data Ingestion'

try :
    logger.info(f'<<<<<<<<<<<<<<< Stage {Stage_Name} Started <<<<<<<<<<<<<<<')
    obj=DataIngestionPipeline()
    df=obj.main()
    logger.info(f'Data Frame Shape after Data Ingestion :{df.shape}')
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(f'Error at Data Ingestion Main ')
    raise e

Stage_Name='Data PreProcessing'

try:
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} started >>>>>>>>>>>>>>>>>>>>>>")
        obj=DataPreProcessingPipeline()
        df=obj.main(df)
        #logger.info(f"shape {df.shape}")
        logger.info(f'Data Frame Shape {df.shape}')
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} Completed Successfully  >>>>>>>>>>>>>>>>>>>>>>")
                
except  Exception as e:
        logger.info(e)
        raise e



Stage_Name='Data Feature Engineering'

try:
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} started >>>>>>>>>>>>>>>>>>>>>>")
        obj=DataFeatureEngineeringPipeline()
        x,y=obj.main(df)
        logger.info(f" X Shape : {x.shape}")
        logger.info(f" Y Shape : {y.shape}")
        logger.info(f"<<<<<<<<<<<<<<<<< Stage :{Stage_Name} Completed Successfully  >>>>>>>>>>>>>>>>>>>>>>")
except  Exception as e:
        logger.info(e)
        raise e