from configparser import RawConfigParser

def get_config():
    path = "../configs/configs.properties"
    parser = RawConfigParser()
    parser.read(path)
    return parser