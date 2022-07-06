import glob
import pandas as pd

from app.configs.yaml_configs import YamlConfigs
from dataset.model.run_bash_scripts import RunBashScripts

class Datasets():
         
    def __init__(self):
        self.rbs = RunBashScripts()
        self.yml = YamlConfigs()
        self.datasets = self.yml.datasets_config()
        self.principal = self.yml.principal_config()
        
    def get_datas(self, ano = '2021'):
            path_data = self.datasets['get_datas']['path_data']
            ama_datas = glob.glob(f'{path_data}/ama/edicoes/{ano}/*/*/*.txt')
            maceio_datas = glob.glob(f'{path_data}/maceio/prefeitura/edicoes/{ano}/*/*/*.txt')

            print(f'the number of txt archive is: {len(ama_datas)}')
            print(f'the number of txt archive is: {len(maceio_datas)}')

            return ama_datas + maceio_datas

    def archive_txt_with_path(self, path):
        file = open(path, "r")
        file = file.read()
        return file  

    def dataframe(self, recived_data):
        if len(recived_data) == 0:
            return 'Your data is empty!'
        datas = pd.DataFrame()
        for path in recived_data:
            file = self.archive_txt_with_path(path)
    #         print(f'path: {path} -  classification: {was_classifield}')
            datas = datas.append({'text': file}, ignore_index=True)
        
        return datas
        
    def merge_e_erros(self, df,error_file_name):
        df_erros = df[df['label'] != df['merge']]
        erros = df_erros[df_erros['predict_proba_label'].apply(max) < 0.9]
        self.salva_dataset_prodigy(erros, error_file_name)
        df['label'] = df['merge']
        return erros, df
    
    def execute(self):
        df = self.get_datas()
        
        return self.dataframe(df)

        