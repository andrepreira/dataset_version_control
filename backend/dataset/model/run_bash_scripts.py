import subprocess

from app.configs.yaml_configs import YamlConfigs

class RunBashScripts():
    def __init__(self):
        self.yml = YamlConfigs()
        self.principal = self.yml.principal_config()
        self.root_path = self.principal['root_path']
        self.path_recipes = f'{self.root_path}/dataset/model/scripts/recipes'
    
    def bash_command(self, cmd):
        subprocess.run(cmd, shell=True, executable='/bin/bash')
        
    def db_in_recipe(self, dataset_name, path):
        cmd = f'bash {self.path_recipes}/db_in_recipe.sh {dataset_name} {path}'
        self.bash_command(cmd)
        print("dataset salvo no banco com prodigy!")
        
    def db_out_recipe(self, dataset_name, jsonl_file_name):
        cmd = f'bash {self.path_recipes}/db_out_recipe.sh {dataset_name} {jsonl_file_name}'
        self.bash_command(cmd)
        print("dataset exportado do prodigy!")
        
    def drop_recipe(self, dataset_name):
        cmd = f'bash {self.path_recipes}/drop_recipe.sh {dataset_name}'
        self.bash_command(cmd)
        print("dataset excluido do prodigy!")

    def ner_train_recipe(self, path, dataset_name):
        cmd = f'bash {self.path_recipes}/ner_train_recipe.sh {path} {dataset_name}'
        self.bash_command(cmd)
        print("Fim do treino do dataset NER do prodigy!")
        
    def textcat_train_recipe(self, path, dataset_name):
        cmd = f'bash {self.path_recipes}/textcat_train_recipe.sh {path} {dataset_name}'
        self.bash_command(cmd)
        print("Fim do treino do dataset de classificacao do prodigy!")
        
    def textcat_manual_recipe(self, dataset_name, path_to_json, label_list):
        cmd = f'bash {self.path_recipes}/textcat_manual_recipe.sh {dataset_name} {path_to_json} {label_list}'
        self.bash_command(cmd)
        print("textcat manual !")
        
    def textcat_manual_recipe(self, dataset_name, path_to_json, label_list):
        cmd = f'bash {self.path_recipes}/textcat_manual_recipe.sh {dataset_name} {path_to_json} {label_list}'
        self.bash_command(cmd)
        print("textcat manual !")