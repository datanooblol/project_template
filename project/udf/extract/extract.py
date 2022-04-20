from udf.utils.utils import *
from udf.utils.configs import *
import pandas as pd
import os

class ExtractData:
    def __init__(self):
        self.conf = get_config()["current_env"]
        self.filename = "titanic"
    
    # def _extract_data(self, source, usage):
    #     DIR = self.conf[source]
    #     if not os.path.exists(DIR):
    #         os.makedirs(DIR)
    #     return pd.read_csv(f"{DIR}/{self.filename}_{usage}_{source}.csv")
    
    def _extract_data(self, usage):
        DIR = self.conf[source]
        if not os.path.exists(DIR):
            os.makedirs(DIR)
        return pd.read_csv(f"{DIR}/{self.filename}_{source}.csv")
    
#     @log_extract
#     def extract_train_raw(self):
#         return self._extract_data(usage="train", source="raw")
#     @log_extract
#     def extract_test_raw(self):
#         return self._extract_data(usage="test", source="raw")
#     @log_extract        
#     def extract_train_interim(self):
#         return self._extract_data(usage="train", source="interim")
#     @log_extract
#     def extract_test_interim(self):
#         return self._extract_data(usage="test", source="interim")
#     @log_extract        
#     def extract_train_processed(self):
#         return self._extract_data(usage="train", source="processed")
#     @log_extract
#     def extract_test_processed(self):
#         return self._extract_data(usage="test", source="processed")
    
    @log_extract
    def extract_raw(self):
        return self._extract_data(source="raw")

    @log_extract
    def extract_feature_store(self):
        return self._extract_data(source="feature_store")
    

