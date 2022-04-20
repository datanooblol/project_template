from udf.utils.utils import *
from udf.pipeline.data_preparation import BasePipeline
from functools import reduce
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

class FeatureEngineering(BasePipeline):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.encoder = {}
        self.method = "train"

    def __call__(self, inputs):
        return self.run(inputs=inputs)
        
    @property
    def _clear_cache(self):
        self.data = {}
    
    @log_transform
    def pass_through(self, inputs):
        return inputs
    
    @log_transform
    def social_status(self, inputs):
        target_col = self.social_status.__name__
        data = inputs.copy()
        title_ser = data["name"].str.extract(r'\s+([a-zA-Z]+)\.+')

        title_dict = {"noble_male":["Jonkheer","Sir","Don"],"noble_female": ["Lady","Countess"], 
                      "military":["Major","Col","Capt"],
                      "believer":["Rev"],
                      "master_male":["Master"], 
                      "married_female":["Mrs"],"single_female":["Miss","Mlle"], "female":["Ms","Mme"],
                      "educated_person":["Dr"], "male":["Mr"]}
        mapped_titles = {}
        for k, v in title_dict.items():
            mapped_titles.update({title:k for title in v})
        data[target_col] = title_ser.squeeze().map(mapped_titles).fillna("unidentified")
        return data.loc[:,[self._id, target_col]]

    @log_transform
    def family_size(self, inputs):
        target_col = self.family_size.__name__
        data = inputs.copy()
        data[target_col] = data["sibsp"] + data["parch"]
        return data.loc[:, [self._id, target_col]]

    def _parallel(self, inputs):
        data = inputs.copy()
        # with ProcessPoolExecutor() as executor:
        with ThreadPoolExecutor() as executor:
            func_list = [self.pass_through, self.social_status, self.family_size,]
            self.data.update({func.__name__:executor.submit(func, inputs=data).result() for func in func_list})

    def _combine(self):
        data = reduce(lambda left,right: pd.merge(left,right,on=self._id), [v for v in self.data.values()])
        return data
    
    @log_transform
    def run(self, inputs):
        data = inputs.copy()
        self._parallel(inputs=data)
        data = self._combine()
        self._clear_cache
        return data