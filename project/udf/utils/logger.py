import logging
from udf.utils.configs import *
import pandas as pd
from functools import wraps

class LogETL:
    def __init__(self, original_func):
        self.original_func = original_func
        self.log_type = "debug"
        self.conf_log = get_config()["log"]
        self.FORMAT = "[%(asctime)s]|%(message)s"
        self.logger = self.get_logger()
    
    def get_logger(self):
        logger = logging.getLogger(self.original_func.__name__)
        
        log_var = {"debug":logging.DEBUG,
                   "info":logging.INFO,}
        logger.setLevel(log_var[self.log_type])

        formatter = logging.Formatter(self.FORMAT)

        file_handler = logging.FileHandler(self.conf_log[self.log_type], mode="a")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger
    
    def _log_process(self, elapsed, module, step, shape):
        """
        message format = epoch|module|func_name|line_no|step|data|shape
        """
        # source = self.original_func.__code__.co_filename.split("/")[-1]
        # module = self.original_func.__module__
        # module = "trasform"
        func_name = self.original_func.__name__
        line_no = self.original_func.__code__.co_firstlineno
        # msg_fmt = f"{source}|{module}|{func_name}|{line_no}|{step}|{data}|{shape}"
        msg_fmt = f"{elapsed:.6f}|{module}|{func_name}|{line_no}|{step}|{shape}"
        self.logger.debug(msg_fmt)
        
    def start_log(self, module, shape, elapsed=""):
        # self._log_process(step="start", data="inputs", shape=shape, elapsed=elapsed)
        self._log_process(elapsed=elapsed, module=module, step="start", shape=shape)
    
    def end_log(self, module, shape, elapsed):
        # self._log_process(step="end", data="outputs", shape=shape, elapsed=elapsed)
        self._log_process(elapsed=elapsed, module=module, step="end", shape=shape)
        
    def epoch_log(self, module, shape, elapsed):
        # self._log_process(step="end", data="outputs", shape=shape, elapsed=elapsed)
        self._log_process(elapsed=elapsed, module=module, step="epoch", shape=shape)
    
    