import os 
import urllib.request as request
import zipfile
from nltkClassifier import logger
from nltkClassifier.Utils.common import get_size
import requests
from io import BytesIO
from nltkClassifier.Config.configuration import DataIngestionConfig


os.chdir("c:\\Users\\rajum\\DATA SCIENCE\\VS\\DrugEfficacy")

class DataIngestion:
    
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    
    def download_file(self):
        # Step 1: Define raw URL and target paths
        zip_url = "https://raw.githubusercontent.com/RS4327/RAWDATA/main/drugsComTrain_raw.zip"
        download_path = "artifacts/data_ingestion/drugsComTrain_raw.zip"
        extract_path = "artifacts/data_ingestion"
        
        # Step 2: Create directories
        os.makedirs(os.path.dirname(download_path), exist_ok=True)

        os.makedirs(extract_path, exist_ok=True)

        # Step 3: Download the ZIP file
        response = requests.get(zip_url)
        response.raise_for_status()  # Raise error for bad status

        with open(download_path, 'wb') as f:
            f.write(response.content)

        #print(f"✅ ZIP file downloaded to: {download_path}")
        #logger.info(f"✅ ZIP file downloaded to: {download_path}")

        # Step 4: Extract ZIP
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        #print(f"✅ ZIP file extracted to: {extract_path}")
        #logger.info(f"✅ ZIP file downloaded to: {extract_path}")
