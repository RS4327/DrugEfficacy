import numpy as np
import pandas as pd
import re
from DrugEfficacy.Config.CongurationManager import DataPreProcessingConfig
from DrugEfficacy.Utils.common import *
from DrugEfficacy import logger


class DataPreProcessing:
    def __init__(self,config:DataPreProcessingConfig):
        self.config=config
         
    def clean_text(self,text):
        if pd.isna(text):
            return ""
        text =text.lower()
        text=re.sub(r"http\S+|www\S+","",text)
        text=re.sub(r"[^a-z0-9\s]"," ",text)
        text=re.sub(r"\s+"," ",text).strip()
        return text
    def process(self,df: pd.DataFrame)->pd.DataFrame:
        create_directories([self.config.root_dir])
        df['clean_review']=df['review'].astype(str).apply(self.clean_text)
        df.dropna(subset=['rating'],inplace=True)
        logger.info(f" Data cleaned and text normalized.")
        return df


