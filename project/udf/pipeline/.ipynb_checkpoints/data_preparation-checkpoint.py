from udf.utils.utils import *
# from functools import reduce
# from sklearn.preprocessing import OneHotEncoder
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
################################        
class BasePipeline:
    def __init__(self):
        self._id = "passengerid"
        self._label = "survived"
        # self._features = []

class PreProcessing(BasePipeline):
    def __init__(self):
        super().__init__()
        self._prep_col_to_drop = ["cabin", "ticket", "embarked"]

    def __call__(self, inputs):
        return self.run(inputs=inputs)
        
    @log_transform
    def lower_colname(self, inputs):
        data = inputs.copy()
        data.columns = data.columns.str.lower()
        return data
    
    
    @log_transform
    def drop_dup(self, inputs):
        return inputs.drop_duplicates()
    
    @log_transform
    def drop_col_na(self, inputs, col_name=None):
        if col_name == None:
            col_name = self._prep_col_to_drop
        return inputs.drop(col_name, axis=1)
    
    @log_transform
    def round_n(self, inputs):
        data = inputs.copy()
        data["fare"] = data["fare"].apply(lambda x: f"{x:.2f}").astype("float")
        return data
    
    @log_transform
    def run(self, inputs):
        data = inputs.copy()
        data = self.lower_colname(inputs=data)
        data = self.round_n(inputs=data)
        data = self.drop_dup(inputs=data)
        data = self.drop_col_na(inputs=data)
        return data