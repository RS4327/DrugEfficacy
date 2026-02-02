from DrugEfficacy import logger
from DrugEfficacy.Pipeline.Stage_D01_DataIngestoin import DataIngestionPipeline
from pathlib import Path
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
Stage_Name='Data Ingestion'

try :
    logger.info(f'<<<<<<<<<<<<<<< Stage {Stage_Name} Started <<<<<<<<<<<<<<<')
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
except Exception as e:
    logger.info(f'Error at Data Ingestion Main ')
    raise e
