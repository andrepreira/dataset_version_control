import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#classificadores
from sklearn.linear_model import SGDClassifier

# Vetorização TD-IDF e pipeline
from sklearn.model_selection import train_test_split
from app.datasets import Datasets

from dataset import RunBashScripts

class Training():
         
    def __init__(self):
        self.rbs = RunBashScripts()
        self.dts = Datasets()
    
    def export_dataset_prodigy(self, dataset_name, jsonl_file_name):
        self.rbs.db_out_recipe(dataset_name, jsonl_file_name)
        path = f'/home/andre-pereira/projects/aisolutions/dataset_version_control/data/interim/{dataset_name}.jsonl'
        return pd.read_json(path, lines=True)
    
    def pipeline_vetorizacao_classificacao(self):
        return Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf', SGDClassifier(loss='modified_huber')),
                    ])
        
    def textcat_sklearn(self, dataset_name, jsonl_file_name, versao):
        df = self.export_dataset_prodigy(dataset_name, jsonl_file_name)
        df = df[df.status ==  'classified']
        x = df.text
        y = df.label
        
        x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.5, random_state=42, shuffle=True, stratify=y)
        
        # Load pipeline treinando versao antiga
        pipeline = self.pipeline_vetorizacao_classificacao()
        
        pipeline.fit(x_train, y_train)
        
        print(f'score = {pipeline.score(x_test, y_test)}')
        
        y_pred_all = pipeline.predict(df.text)
        
        df['merge'] = y_pred_all
        
        y_pred_proba_all = pipeline.predict_proba(df.text)

        df['predict_proba_label'] = list(y_pred_proba_all)
        
        joblib.dump(pipeline, f'/home/andre-pereira/projects/aisolutions/dataset_version_control/dataset/pipeline/pipeline_v{str(versao)}.pkl')
        df.to_pickle(f'/home/andre-pereira/projects/aisolutions/dataset_version_control/dataset/dataset_corrigido_v{str(versao)}.pkl')
        return df
    def run_train(self):
        pass
    
if __name__ == '__main__':
    tr = Training()
    
    dataset_name = 'licitacoes_contratos_regex'
    json_file_name = dataset_name
    df = tr.textcat_sklearn(dataset_name, json_file_name, 1)
    
    dataset_erros = 'erros_licitacoes_contratos_v1'
    erros, df = tr.dts.merge_e_erros(df, dataset_erros)        
    dataset_name = 'licitacoes_contratos_v1'
    df = tr.dts.salva_dataset_prodigy(df, dataset_name)
    print(erros)
    print(df)
    del df, erros