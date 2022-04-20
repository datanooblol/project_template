from udf.utils.logger import *
# from udf.load.load import LoadData
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
        else:
            LOG.start_log(module="transform", shape=(0,0), elapsed=0)
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

# @log_load
# def project_init():
#     columns = pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv", 
#                 usecols=None).columns
#     dtype_list = [np.int16, np.int8, np.int16, str, str, np.float16, np.int8, np.int8, str, np.float64, str, str]
#     dtype_col = {k:v for k, v in zip(columns, dtype_list)}
#     data = pd.read_csv("https://raw.githubusercontent.com/datanooblol/toy_dataset/master/titanic/titanic-train.csv", 
#                 usecols=None,
#                dtype=dtype_col)
#     ldt = LoadData()
#     ldt.load_raw(inputs=data)
#     return data
    