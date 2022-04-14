import pandas as pd
import rubrix as rb
from datetime import datetime

from database.utils  import *
from classificacao.classificacao_ml import *
from classificacao.classificacao_regex import *

DATASET_ERROS_RUBRIX = "erros_rubrix"

class Classificador:
    
    def __init__(self, id_dataset, conn):
        self.id_dataset = id_dataset
        self.conn = conn
    
    def pega_itens(self):
        item = import_table('item', self.conn)
        query = db.select([item.columns.id,item.columns.texto]).where(item.columns.id_dataset == self.id_dataset)
        r = self.conn.execute(query).fetchall()
        df = pd.DataFrame(r)
        df.columns = r[0].keys()
        return df

    def insere_id_versao(self, df, id_versao):
        df['id_versao'] = id_versao
        return df

    def insere_labels(self, name_table, conn, data, id_versao, label_name='label', msg='dados salvos'):
        data = self.insere_id_versao(data, id_versao)
        data = data.rename(columns = {label_name: 'label'})
        data['id_item'] = data.id
        col = ['label', 'id_item', 'id_versao']
        data = data[col]
        data.to_sql(name_table, conn, if_exists='append', index = False)
        print(msg)

    def extraindo_erros_dataset(self, df, pipeline):
        selection = df['label_regex'] != df['predict_classification']
        
        idxs = list(enumerate(selection))
        idx_off_diag_conf_matrix = [i for i,p in idxs if p]

        erros = df.query('index in @idx_off_diag_conf_matrix')
        erros_prob = pipeline.predict_proba(erros.texto)
        
        print('A quantidade de dados classificados com erro neste treinamento é: {} '.format(len(idx_off_diag_conf_matrix)))
        erros['probabilities'] = list(erros_prob)
        return erros

    def envio_rubrix(self, dataset, pipeline, agent_name='nome do agente'):
        data_atual = datetime.now()
        rb.init(api_url="http://localhost:6900")

        # Build the Rubrix records
        records = [
            rb.TextClassificationRecord(
                id=idx,
                inputs=row['texto'],
                prediction=list(zip(pipeline.classes_, row['probabilities'])),
                prediction_agent=agent_name,

            )
            for idx, row in dataset.iterrows()
        ]

        # Log the records
        rb.log(records, name=DATASET_ERROS_RUBRIX, 
            tags={
                "dataset": "erros classificacao diarios oficiais 2021",
                "metodologia": "dados off diagonal da matriz de confusao",
                "data": data_atual.strftime('%d/%m/%Y')
                },
            )

    def run(self):
        # pega itens no banco
        item = self.pega_itens()
        # classifica com regex e retorna dataset com colunas: texto, labels, status
        df = regex(item)
        df, sgd_pipeline = predict_ml(df)
        
        df_erros = self.extraindo_erros_dataset(df, sgd_pipeline)

        #envio de dados rubrix
        self.envio_rubrix(df_erros, sgd_pipeline, 'DecisionTreeClassifier')

        #regex
        self.insere_labels('classificados', self.conn, df, 1, 'label_regex', 'dados regex salvos no banco!!')
                
        #machine learning
        self.insere_labels('classificados', self.conn, df, 2, 'predict_classification', 'dados machine learning salvos no banco!!')

        #diff entre regex e machine learning
        self.insere_labels('classificados', self.conn, df_erros, 3, 'predict_classification', 'dados diff salvos no banco!!')

