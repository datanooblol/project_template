from udf.utils.utils import *
from udf.pipeline.data_preparation import BasePipeline
from functools import reduce
from sklearn.preprocessing import OneHotEncoder
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

class FeatureEngineering(BasePipeline):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.encoder = {}
        self.method = "train"

    @property
    def _clear_cache(self):
        self.data = {}
    
    @log_transform
    def label(self, inputs):
        data = inputs.loc[:,[self._id, self._label]].copy()
        return data
    
    def _ohe(self, inputs, target_col):
        vec = inputs.drop(self._id, axis=1).values.reshape(-1,1)
        if self.method == "train":
            self.encoder.update({target_col:OneHotEncoder(sparse=False).fit(vec)})
            
        vec = self.encoder[target_col].transform(vec)
        # ohe_cols = self.encoder[target_col].get_feature_names_out([target_col])
        data = pd.DataFrame(vec, 
                            # columns=ohe_cols,
                            columns=self.encoder[target_col].get_feature_names_out([target_col]),
                            # columns=self.encoder[target_col].get_feature_names_out(target_col)
                            dtype=np.int8,
                            index=inputs.loc[:,self._id]).reset_index()
        return data
    
    @log_transform
    def sex_ohe(self, inputs):
        target_col = self.sex_ohe.__name__
        data = inputs.loc[:,[self._id, "sex"]].copy()
        data = self._ohe(inputs=data, target_col=target_col)
        return data
        
    def _social_status(self, inputs):
        data = inputs.copy()
        target_col = "social_status"
        title_ser = data["name"].str.extract(r'\s+([a-zA-Z]+)\.+')

        title_dict = {"noble_male":["Jonkheer","Sir","Don"],"noble_female": ["Lady","Countess"], 
                      "military":["Rev","Major","Col","Capt"],
                      "master_male":["Master"], 
                      "married_female":["Mrs"],"single_female":["Miss","Mlle"], "female":["Ms","Mme"],
                      "educated_person":["Dr"], "male":["Mr"]}
        mapped_titles = {}
        for k, v in title_dict.items():
            mapped_titles.update({title:k for title in v})
        data[target_col] = title_ser.squeeze().map(mapped_titles).fillna("unidentified")
        return data.loc[:,[self._id, target_col]]
    
    @log_transform
    def social_status_ohe(self, inputs):
        target_col = self.social_status_ohe.__name__
        data = inputs.loc[:,[self._id, "name"]].copy()
        data = self._social_status(inputs=data)
        data = self._ohe(inputs=data, target_col=target_col)
        return data

    def _family_size(self, inputs):
        data = inputs.copy()
        target_col = "family_size"
        data[target_col] = data["sibsp"] + data["parch"]
        return data.loc[:, [self._id, target_col]]
    
    @log_transform
    def family_size_ohe(self, inputs):
        target_col = self.family_size_ohe.__name__
        data = inputs.loc[:,[self._id, "sibsp", "parch"]].copy()
        data = self._family_size(inputs=data)
        data = self._ohe(inputs=data, target_col=target_col)
        return data
    
    @log_transform 
    def pclass_ohe(self, inputs):
        target_col = self.pclass_ohe.__name__
        data = inputs.loc[:,[self._id, "pclass"]].copy()
        data = self._ohe(inputs=data, target_col=target_col)
        return data
    
    @log_transform
    def pass_through(self, inputs):
        data = inputs.loc[:,[self._id, "age", "fare"]].copy()
        return data
        
    # @log_transform
    def _parallel(self, inputs):
        data = inputs.copy()
        # with ProcessPoolExecutor() as executor:
        with ThreadPoolExecutor() as executor:
            func_list = [self.label,
                         self.sex_ohe,
                         self.pclass_ohe,
                         self.social_status_ohe,
                         self.family_size_ohe,
                         self.pass_through]
            self.data.update({func.__name__:executor.submit(func, inputs=data).result() for func in func_list})

    def _combine(self):
        data = reduce(lambda left,right: pd.merge(left,right,on=self._id), [v for v in self.data.values()])
        return data
    
    @log_transform
    def fe(self, inputs):
        data = inputs.copy()
        self._parallel(inputs=data)
        data = self._combine()
        
        self._clear_cache
        return data