import numpy as np
import pandas as pd
from DrugEfficacy.Config.CongurationManager import ConfigurationManagerConfig
from DrugEfficacy.Utils.common import *
from DrugEfficacy.Entity.Entity_Config import *
from DrugEfficacy import logger
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

class DataFeatureEnginerring:
    def __init__(self,config: DataFeatureEngineeringConfig,max_features=10000):
        self.config=config
        self.max_features=max_features
        self.vectorizer=None
    
    def create_target(self,df:pd.DataFrame,threshold=4.0)->pd.DataFrame:
         df['target']=(df['rating']>=threshold).astype(int)
         logger.info(f"Target Variable Created")
         logger.info(df.head(2))
         return df
    def build_vectorizer(self,df: pd.DataFrame)->pd.DataFrame:
        self.vectorizer=TfidfVectorizer(max_features=self.max_features,ngram_range=(1,2),min_df=3)
        x=self.vectorizer.fit_transform(df['clean_review'])
        logger.info(f"TF - IDF Freatures created .shape {x.shape}")
        joblib.dump(self.vectorizer, self.config.output_data_path)
        print(f"Vectorizer saved at {self.config.output_data_path}")
        return x,df['target']
