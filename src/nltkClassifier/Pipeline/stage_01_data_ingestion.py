from nltkClassifier.Entity.config_entity import DataIngestionConfig
from nltkClassifier.Config.configuration import ConfiguraitonManager
from nltkClassifier.Components.data_ingestion import DataIngestion
from nltkClassifier import logger

Stage_Name ='Data Ingestion'

class DataIngestionPipeLine:
    def __init__(self):
        pass
    def main(self):

        try:
            config = ConfiguraitonManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            
        except Exception as e:
            raise e


if __name__=="__main__":
    try :
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataIngestionPipeLine()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.info(e)
        raise e
        


