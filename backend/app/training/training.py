import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#classificadores
from sklearn.linear_model import SGDClassifier

# Vetorização TD-IDF e pipeline
from sklearn.model_selection import train_test_split

from app.configs.yaml_configs import YamlConfigs
from app.datasets.datasets import Datasets
from dataset.model.run_bash_scripts import RunBashScripts

class Training():
         
    def __init__(self):
        self.rbs = RunBashScripts()
        self.dts = Datasets()
        self.yml = YamlConfigs()
        self.training = self.yml.training_config()
        self.principal = self.yml.principal_config()
        self.root_path = self.principal['root_path']
    
    def export_dataset_prodigy(self, dataset_name, jsonl_file_name):
        self.rbs.db_out_recipe(dataset_name, jsonl_file_name)
        path = f'{self.root_path}/data/interim/{dataset_name}.jsonl'
        return pd.read_json(path, lines=True)
    
    def pipeline_vetorizacao_classificacao(self):
        return Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf', SGDClassifier(loss='modified_huber')),
                    ])
        
    def textcat_sklearn_v1(self, dataset_name, jsonl_file_name, version):
        df = self.export_dataset_prodigy(dataset_name, jsonl_file_name)
        df = df[df.status ==  'classified']
        x = df.text
        y = df.label
        
        x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=self.training['test_size'], random_state=self.training['random_state'], shuffle=True, stratify=y)
        
        # Load pipeline treinando versao antiga
        pipeline = self.pipeline_vetorizacao_classificacao()
        
        pipeline.fit(x_train, y_train)
        
        print(f'score = {pipeline.score(x_test, y_test)}')
        
        y_pred_all = pipeline.predict(df.text)
        
        df['merge'] = y_pred_all
        
        y_pred_proba_all = pipeline.predict_proba(df.text)

        df['predict_proba_label'] = list(y_pred_proba_all)
        
        joblib.dump(pipeline, f'{self.root_path}/dataset/pipeline/pipeline_v{str(version)}.pkl')
        df.to_pickle(f'{self.root_path}/dataset/dataset_corrigido_v{str(version)}.pkl')
        del x,y,x_train, x_test, y_train, y_test
        return df
    
    def textcat_sklearn_other_versions(self, dataset_name, jsonl_file_name, version):
        df = self.export_dataset_prodigy(dataset_name, jsonl_file_name)
        df = df[df.status ==  'classified']
        x = df.text
        y = df.label
        
        x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=self.training['test_size'], random_state=self.training['random_state'], shuffle=True)
        
       # Vetorização TD-IDF e pipeline
        pipeline = joblib.load(f'{self.root_path}/dataset/pipeline/pipeline_v{str(version - 1)}.pkl')
        
        pipeline.fit(x_train, y_train)
        
        print(f'score = {pipeline.score(x_test, y_test)}')
        
        y_pred_all = pipeline.predict(df.text)
        
        df['merge'] = y_pred_all
        
        y_pred_proba_all = pipeline.predict_proba(df.text)

        df['predict_proba_label'] = list(y_pred_proba_all)
        
        joblib.dump(pipeline, f'{self.root_path}/dataset/pipeline/pipeline_v{str(version)}.pkl')
        df.to_pickle(f'{self.root_path}/dataset/dataset_corrigido_v{str(version)}.pkl')
        del x,y,x_train, x_test, y_train, y_test
        return df
    
    def run_train_v1(self, dataset_file_name, version_number):
        dataset_name = f'{dataset_file_name}_regex'
        json_file_name = dataset_name
        df = self.textcat_sklearn_v1(dataset_name, json_file_name, 1)
        
        dataset_erros = f'erros_{dataset_file_name}_v{version_number}'
        erros, df = self.dts.merge_e_erros(df, dataset_erros)
                
        dataset_name = f'{dataset_file_name}_v{version_number}'
        df = self.dts.salva_dataset_prodigy(df, dataset_name)
        print(erros)
        print(df)
        del df, erros
    
    def run_train_other_versions(self, dataset_file_name, version_number):
            dataset_name = f'{dataset_file_name}_v{version_number - 1}'
            json_file_name = dataset_name
            df = self.textcat_sklearn_other_versions(dataset_name, json_file_name, version_number)
            
            dataset_erros = f'erros_{dataset_file_name}_v{version_number}'
            erros, df = self.dts.merge_e_erros(df, dataset_erros)
                    
            dataset_name = f'{dataset_file_name}_v{version_number}'
            df = self.dts.salva_dataset_prodigy(df, dataset_name)
            print(erros)
            print(df)
            del df, erros
            
    def execute(self):
        pass    
    
if __name__ == '__main__':
    tr = Training()
    
    # tr.run_train_v1('licitacoes_contratos', 1)
    # tr.run_train_other_versions('licitacoes_contratos', 2)
    # tr.run_train_other_versions('licitacoes_contratos', 3)
    # tr.run_train_other_versions('licitacoes_contratos', 4)
    # tr.run_train_other_versions('licitacoes_contratos', 5)
    