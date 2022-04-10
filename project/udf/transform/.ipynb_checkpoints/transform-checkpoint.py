from udf.utils.utils import *
################################        
class PreProcessing:
    def __init__(self):
        pass
    @log_transform
    # @get_time
    def test_a(self, inputs):
        outputs = inputs
        return outputs.head(15)
        
    @log_transform
    # @get_time
    def test_b(self, inputs):
        outputs = inputs
        return outputs.head(10)
        
    def runner(self, inputs):
        data = inputs.copy()
        data = self.test_a(inputs=data)
        data = self.test_b(inputs=data)
        