from decouple import config
import os
import yaml

class YamlConfigs():
    
    def __init__(self):
        self.CONFIG_PATH = f"{config('ROOTPATH')}/app/configs/"
    
    def load_config(self, config_name):
        with open(os.path.join(self.CONFIG_PATH, config_name)) as file:
            config = yaml.safe_load(file)

        return config
    
    def principal_config(self):
        return self.load_config('principal.yaml')
        
    def datasets_config(self):
        return self.load_config('datasets.yaml')
        
    def training_config(self):
        return self.load_config('training.yaml')
        
    def experiment_config(self):
        return self.load_config('experiment.yaml')
        
    