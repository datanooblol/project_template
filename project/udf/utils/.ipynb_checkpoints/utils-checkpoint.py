from udf.utils.logger import *
from functools import wraps
import pandas as pd
import numpy as np
import time
    
def log_transform(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        LOG = LogETL(func)
        if "inputs" in kwargs.keys():
            LOG.start_log(module="transform", shape=kwargs["inputs"].shape, elapsed=0)
        start = time.time()
        outputs = func(*args,**kwargs)
        end = time.time()
        elapsed = end-start
        if isinstance(outputs, (pd.DataFrame, pd.Series, np.array)):
            LOG.end_log(module="transform", shape=outputs.shape, elapsed=elapsed)
        return outputs
    return wrapper

def log_extract(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        LOG = LogETL(func)
        start = time.time()
        outputs = func(*args,**kwargs)
        end = time.time()
        elapsed = end-start
        LOG.epoch_log(module="extract", shape=outputs.shape, elapsed=elapsed)
        return outputs
    return wrapper

def log_load(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        LOG = LogETL(func)
        inputs = kwargs["inputs"].shape
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        elapsed = end-start
        LOG.epoch_log(module="load", shape=inputs, elapsed=elapsed)
    return wrapper

# def get_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         outputs = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__}|excecuted in {end-start:.4f}")
#         return outputs
#     return wrapper
    
    
