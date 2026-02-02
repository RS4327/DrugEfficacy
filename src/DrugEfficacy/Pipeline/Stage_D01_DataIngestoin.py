from DrugEfficacy.Components.Data_Ingestion import DataIngestion
from DrugEfficacy.Config.CongurationManager import ConfigurationManagerConfig

from DrugEfficacy import logger


Stage_Name='Data Ingestion'

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManagerConfig()
            data_ingestion_config=config.GetDataIngestionConfig()
            data_ing=DataIngestion(config=data_ingestion_config)
            data_load=data_ing.DataLoading()
            
        except Exception as e:
            logger.info(f"Error at DataIngestionPipline")
            raise e


if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e

        
        
            
