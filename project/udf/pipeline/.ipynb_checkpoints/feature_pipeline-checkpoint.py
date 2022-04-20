from udf.pipeline.data_preparation import *
from udf.pipeline.feature_engineering import *
from udf.load.load import *

class FeaturePipeline:
    def __init__(self):
        self.prep = PreProcessing()
        self.fe = FeatureEngineering()
        self.load = LoadData()

    def __call__(self, inputs, *args, **kwargs):
        return self.run(inputs=inputs, *args, **kwargs)
        
    def run(self, inputs, save=True, display=True, *args, **kwargs):
        data = inputs.copy()
        data = self.prep(inputs=data)
        data = self.fe(inputs=data)
        if save == True:
            self.load.load_feature_store(inputs=data)
        if display == True:
            return data