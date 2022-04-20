import pandas as pd
from udf.utils.configs import *
from udf.utils.utils import *
import os

# def load_raw_data():
#     # filepath = "https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv"
#     # data = pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-test.csv")
    
#     DIR = get_config()["data"]["raw"]
#     filename = "titanic"
#     pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv").to_csv(f"{DIR}/{filename}_train_raw.csv", index=False)
#     pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-test.csv").to_csv(f"{DIR}/{filename}_test_raw.csv", index=False)
#     # data.to_csv(f"{DIR}/titanic_train_raw.csv")
    
# load_raw_data()

class LoadData:
    def __init__(self):
        self.conf = get_config()["current_env"]
        self.filename = "titanic"
    
    # def _load_data(self, inputs, usage, source):
    #     DIR = self.conf[source]
    #     if not os.path.exists(DIR):
    #         os.makedirs(DIR)
    #     return inputs.to_csv(f"{DIR}/{self.filename}_{usage}_{source}.csv", index=False)
    def _load_data(self, inputs, source):
        DIR = self.conf[source]
        if not os.path.exists(DIR):
            os.makedirs(DIR)
        return inputs.to_csv(f"{DIR}/{self.filename}_{source}.csv", index=False)
    
#     @log_load
#     def load_train_raw(self, inputs):
#         return self._load_data(inputs=inputs, usage="train", source="raw")
    
#     @log_load
#     def load_test_raw(self, inputs):
#         return self._load_data(inputs=inputs, usage="test", source="raw")
    
#     @log_load
#     def load_train_interim(self, inputs):
#         return self._load_data(inputs=inputs, usage="train", source="interim")
#     @log_load
#     def load_test_interim(self, inputs):
#         return self._load_data(inputs=inputs, usage="test", source="interim")
#     @log_load
#     def load_train_processed(self, inputs):
#         return self._load_data(inputs=inputs, usage="train", source="processed")
#     @log_load
#     def load_test_processed(self, inputs):
#         return self._load_data(inputs=inputs, usage="test", source="processed")
    
    # use this
    @log_load
    def load_raw(self, inputs):
        return self._load_data(inputs=inputs, source="raw")
    
    @log_load
    def load_feature_store(self, inputs):
        return self._load_data(inputs=inputs, source="feature_store")
    
@log_extract
def project_init():
    columns = pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv", 
                usecols=None).columns
    dtype_list = [np.int16, np.int8, np.int16, str, str, np.float16, np.int8, np.int8, str, np.float64, str, str]
    dtype_col = {k:v for k, v in zip(columns, dtype_list)}
    data = pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv", 
                usecols=None,
               dtype=dtype_col)
    ldt = LoadData()
    ldt.load_raw(inputs=data)
    return data