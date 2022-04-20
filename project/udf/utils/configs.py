from configparser import RawConfigParser

def get_config():
    conf_path = "../configs/configs.properties"
    parser = RawConfigParser()
    parser.read(conf_path)
    return parser

def set_env(env="dev"):
    conf_path = "../configs/configs.properties"
    parser = RawConfigParser()
    parser.read(conf_path)
    parser[f"current_env"] = parser[f"{env}_env"]
    with open(conf_path,"w") as configfile:
        parser.write(configfile)

class ConMan:
    def __init__(self, 
                 conf_path="../configs/configs.properties"):
        self.conf_path = conf_path
        
        
    def set_env(self, env="dev"):
        # path = "../configs/configs.properties"
        parser = RawConfigParser()
        parser.read(self.conf_path)
        parser[f"current_env"] = parser[f"{env}_env"]
        with open(self.conf_path,"w") as configfile:
            parser.write(configfile)
        
    