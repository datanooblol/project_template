from udf.load.load import *
from udf.extract.extract import *
from sklearn.preprocessing import StandardScaler, Normalizer, PowerTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class BaseExperiment:
    def __init__(self):
        self.scaler = {}
        self.encoder = {}
    
    def _ohe(self, inputs):
        pass
    
    
    def fit(self, inputs, target_col):
        pass
    
    def transform(self, inputs, target_col):
        pass
    
    def fit_transform(self, inputs, target_col):
        self.fit(inputs=inputs, target_col=target_col)
        return self.transform(inputs=inputs, target_col=target_col)
    
class Experiment(BaseExperiment):
    def __init__(self):
        super().__init__()