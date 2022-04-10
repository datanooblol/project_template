import pandas as pd
from udf.utils.configs import *
from udf.utils.utils import *

def load_raw_data():
    # filepath = "https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv"
    # data = pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-test.csv")
    
    DIR = get_config()["data"]["raw"]
    filename = "titanic"
    pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv").to_csv(f"{DIR}/{filename}_train_raw.csv", index=False)
    pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-test.csv").to_csv(f"{DIR}/{filename}_test_raw.csv", index=False)
    # data.to_csv(f"{DIR}/titanic_train_raw.csv")
    
load_raw_data()

class LoadData:
    def __init__(self):
        self.conf = get_config()["data"]
        self.filename = "titanic"
    
    def _load_data(self, inputs, usage, source):
        DIR = self.conf[source]
        return inputs.to_csv(f"{DIR}/{self.filename}_{usage}_{source}.csv", index=False)
    @log_load
    def load_train_interim(self, inputs):
        return self._load_data(inputs=inputs, usage="train", source="interim")
    @log_load
    def load_test_interim(self, inputs):
        return self._load_data(inputs=inputs, usage="test", source="interim")
    @log_load
    def load_train_processed(self, inputs):
        return self._load_data(inputs=inputs, usage="train", source="processed")
    @log_load
    def load_test_processed(self, inputs):
        return self._load_data(inputs=inputs, usage="test", source="processed")