
from app.configs.yaml_configs import YamlConfigs
from dataset.model.run_bash_scripts import RunBashScripts

class Spacy():
    
    def __init__(self):
        self.rbs = RunBashScripts()
        self.principal = YamlConfigs().principal_config()
        self.root_path = self.principal['root_path']
    
    def spacy_train_textcat(self, dataset_name, data_to_load):
        path = f'{self.root_path}/dataset/model/model_{dataset_name}_textcat'
        self.rbs.textcat_train_recipe(path, data_to_load)
        
    # def spacy_ner_manual_textcat(self, dataset_name, data_to_load):
    #     path = f'{self.root_path}/dataset/model/model_{dataset_name}_textcat'
    #     self.rbs.textcat_ner_manual_recipe(path, data_to_load)
        
    # def spacy_ner_correct_textcat(self, dataset_name, data_to_load):
    #     path = f'{self.root_path}/dataset/model/model_{dataset_name}_textcat'
    #     self.rbs.textcat_ner_correct_recipe(path, data_to_load)
        
    # def spacy_ner_teach_textcat(self, dataset_name, data_to_load):
    #     path = f'{self.root_path}/dataset/model/model_{dataset_name}_textcat'
    #     self.rbs.textcat_ner_teach_recipe(path, data_to_load)

    def spacy_train_ner(self, dataset_name, data_to_load):
        path = f'{self.root_path}/dataset/model/model_{dataset_name}_ner'
        self.rbs.ner_train_recipe(path, data_to_load)

if __name__ == '__main__':
    spcy = Spacy()
    dataset_erros_list ='''erros_licitacoes_contratos_v5'''
    spcy.spacy_train_textcat(dataset_erros_list,'licitacoes_contratos')