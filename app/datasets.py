import glob
import pandas as pd

from dataset import RunBashScripts
from models.EventSearchLicitacaoContrato import EventSearcher

class Datasets():
         
    def __init__(self):
        self.rbs = RunBashScripts()
        self.event = EventSearcher()
        
    def get_datas(self, ano = '2021'):
            ama_datas = glob.glob(f'/home/andre-pereira/projects/data_science/materias/executivo/municipal/ama/edicoes/{ano}/*/*/*.txt')
            maceio_datas = glob.glob(f'/home/andre-pereira/projects/data_science/materias/executivo/municipal/maceio/prefeitura/edicoes/{ano}/*/*/*.txt')

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

    def regex(self, df):
        datas = pd.DataFrame()
        for idx, row in df.iterrows():
            text = row['text']
            was_classifield =  self.event.search(text)
            datas = datas.append({'text': text, 'label': was_classifield}, ignore_index=True)
        
        datas['status'] = datas['label'].apply(lambda x: 'classified' if x else 'unclassified')
        return datas

    def extraindo_erros_dataset(df, pipeline, versao):
            df2 = df[df['label'] != df['predict_classification']]
            erros = df2[df2['predict_proba_label'].apply(max) < 0.9]

            erros_prob = pipeline.predict_proba(erros.text)
            
            print('A quantidade de dados classificados com erro neste treinamento é: {} '.format(len(erros)))
            erros['probabilities'] = list(erros_prob)
            erros.to_pickle(f'./versiona_licitacoes_contratos_sgd/dataset_erros/dataset_erros_v{str(versao)}.pkl')
            
            return erros
    def write_answer_field(self, df):
        df['answer'] = df['label'].apply(lambda x: 'accept' if x else 'reject')
        return df
                
    
    def salva_dataset_prodigy(self, df, dataset_name):
        df = df[df.status ==  'classified']
        df = df[['text', 'label', 'status']]
        df = self.write_answer_field(df)
        path = f'/home/andre-pereira/projects/aisolutions/dataset_version_control/data/interim/{dataset_name}.jsonl'
        df.to_json(path, orient='records', lines=True)
        self.rbs.db_in_recipe(dataset_name, path)
        return df
    
    def merge_e_erros(self, df,error_file_name):
        df_erros = df[df['label'] != df['merge']]
        erros = df_erros[df_erros['predict_proba_label'].apply(max) < 0.9]
        self.salva_dataset_prodigy(erros, error_file_name)
        df['label'] = df['merge']
        return erros, df
    
if __name__ == '__main__':
    
    dts = Datasets()
    
    df = dts.get_datas()
    
    df = dts.dataframe(df)

    df = dts.regex(df)
    
    dataset_name = 'licitacoes_contratos_regex'
    
    df = dts.salva_dataset_prodigy(df, dataset_name)
    
    print(df)
    del df