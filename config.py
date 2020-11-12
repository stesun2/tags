import os
from os.path import dirname, join
import yaml

def load_config(config_file):
    return yaml.safe_load(open(join(dirname(__file__), config_file)))
