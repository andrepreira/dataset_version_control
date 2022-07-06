import pandas as pd
import joblib
import spacy

from app import YamlConfigs, Spacy

class TextcatExperiment():
    
    def __init__(self):
        self.yml = YamlConfigs()
        self.experiment = self.yml.experiment_config()
    
    def train_model_textcat(self):
        pass

    def annotate_manually_textcat(self):
        pass

    def create_traning_data_textcat(self, dataset_name, spacy_model, data_to_load):
        pass
    
    def collect_best_traning_data_textcat(self, dataset_name, spacy_model, data_to_load):
        pass

    def execute(self):
        pass        
