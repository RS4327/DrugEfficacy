from nltkClassifier import logger
from nltkClassifier.Pipeline.stage_01_data_ingestion import DataIngestionPipeLine
from nltkClassifier.Pipeline.stage_02_data_validation import DataValidationPipeLine

Stage_Name ='Data Ingestion'

try :
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataIngestionPipeLine()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e


Stage_Name='Data Validation'

try :
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataValidationPipeLine()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(e)
    raise e