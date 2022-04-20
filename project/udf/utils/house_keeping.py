import shutil
import os
from udf.utils.configs import *

class HouseKeeping:
    def __init__(self):
        pass
    
    def _remove_directory(self, DIR):
        if os.path.exists(DIR):
            shutil.rmtree(DIR)
    
    def remove_logs(self):
        DIR = get_config()["current_env"]["logs"]
        self._remove_directory(DIR)