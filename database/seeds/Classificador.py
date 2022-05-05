import pandas as pd
import rubrix as rb
from datetime import datetime

from database.utils  import *

class Classificador:
    
    def __init__(self, id_dataset, conn, nome_rubrix):
        self.id_dataset = id_dataset
        self.conn = conn
        self.nome_rubrix = nome_rubrix
    
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
        df2 = df[df['label'] != df['predict_classification']]
        erros = df2[df2['predict_proba_label'].apply(max) < 0.9]

        erros_prob = pipeline.predict_proba(erros.texto)
        
        print('A quantidade de dados classificados com erro neste treinamento é: {} '.format(len(erros)))
        erros['probabilities'] = list(erros_prob)
        return erros

    def envio_rubrix(self, dataset, pipeline, agent_name='nome do agente'):
        data_atual = datetime.now()
        rb.init(api_url="http://localhost:6900")

        # Build the Rubrix records
        records = [
            rb.TextClassificationRecord(
                id=idx,
                inputs={'id': row['id'], 'texto': row['texto']},
                prediction=list(zip(pipeline.classes_, row['probabilities'])),
                prediction_agent=agent_name,

            )
            for idx, row in dataset.iterrows()
        ]

        # Log the records
        rb.log(records, name=self.nome_rubrix, 
            tags={
                "dataset": "erros classificacao diarios oficiais 2021",
                "metodologia": "dados off diagonal da matriz de confusao e com probabilidade menor que 90%",
                "data": data_atual.strftime('%d/%m/%Y')
                },
            )
