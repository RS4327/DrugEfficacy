from nltkClassifier import logger
from nltkClassifier.Pipeline.stage_01_data_ingestion import DataIngestionPipeLine

Stage_Name ='Data Ingestion'

try :
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataIngestionPipeLine()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e