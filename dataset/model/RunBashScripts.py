import subprocess
import argparse

class RunBashScripts():
    def __init__(self):
        self.path_recipes = '/home/andre-pereira/projects/aisolutions/dataset_version_control/dataset/model/scripts/recipes'
    
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
        print("dataset exportado do prodigy!")