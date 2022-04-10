from udf.utils.utils import *
from udf.utils.configs import *
import pandas as pd

class ExtractData:
    def __init__(self):
        self.conf = get_config()["data"]
        self.filename = "titanic"
    
    def _extract_data(self, source, usage):
        DIR = self.conf[source]
        return pd.read_csv(f"{DIR}/{self.filename}_{usage}_{source}.csv")
    @log_extract
    def extract_train_raw(self):
        return self._extract_data(usage="train", source="raw")
    @log_extract
    def extract_test_raw(self):
        return self._extract_data(usage="test", source="raw")
    @log_extract        
    def extract_train_interim(self):
        return self._extract_data(usage="train", source="interim")
    @log_extract
    def extract_test_interim(self):
        return self._extract_data(usage="test", source="interim")
    @log_extract        
    def extract_train_processed(self):
        return self._extract_data(usage="train", source="processed")
    @log_extract
    def extract_test_processed(self):
        return self._extract_data(usage="test", source="processed")
    

